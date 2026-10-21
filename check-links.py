#!/usr/bin/env python3
"""
Check every external link in index.html.

139 links will rot over time, and a dead link is the fastest way to lose a
beginner's trust. Run this before each update.

    python3 check-links.py                 # check everything
    python3 check-links.py --fast          # HEAD only, skip the GET fallback
    python3 check-links.py --workers 16    # more concurrency (default 8)
    python3 check-links.py --file other.html

Exit code is 1 if any link is broken, so it can gate a release in CI.
Standard library only — nothing to install.
"""
from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

# Some sites reject the default Python agent outright.
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")
TIMEOUT = 15

# Hosts that commonly refuse automated HEAD/GET even from a browser agent.
# A failure here is reported as SKIP, not as a broken link, to avoid false alarms.
BOT_HOSTILE = {
    "www.linkedin.com", "linkedin.com", "twitter.com", "x.com",
    "www.udemy.com", "udemy.com", "www.coursera.org",
    # These serve fine in a browser but return 403/404 to automated requests.
    # PortSwigger in particular answers 404 rather than 403, which makes a naive
    # checker report the Web Security Academy as dead. Verified by hand 2026-10-21.
    "portswigger.net", "www.hackthebox.com", "hackthebox.com",
    "www.kaggle.com", "kaggle.com", "tryhackme.com", "www.tryhackme.com",
    "adsecurity.org", "ctf.hacker101.com", "gdpr-info.eu",
    "csrc.nist.gov", "www.nist.gov", "nist.gov",   # also answer 404 to bots
    "docs.zeek.org",
}

# Not real destinations — preconnect/resource hints that 404 at their bare domain.
NOT_LINKS = {"fonts.googleapis.com", "fonts.gstatic.com"}

URL_RE = re.compile(r'https?://[^\s"\'<>)\\]+')


def extract(path: str) -> list[str]:
    """Pull URLs from anywhere in the file — hrefs AND JavaScript data."""
    text = open(path, encoding="utf-8", errors="ignore").read()
    urls = set()
    for raw in URL_RE.findall(text):
        u = raw.rstrip(".,;:!?)]}'\"")
        # skip template placeholders like https://x/'+id+'
        if "'+" in u or '"+' in u or "${" in u:
            continue
        if urlparse(u).netloc:
            urls.add(u)
    return sorted(urls)


def check(url: str, fast: bool) -> tuple[str, str, str]:
    """Return (status, url, detail). status in OK/REDIRECT/DEAD/SKIP."""
    host = urlparse(url).netloc.lower()
    if host in NOT_LINKS:
        return ("SKIP", url, "resource hint, not a destination")
    if host in BOT_HOSTILE:
        return ("SKIP", url, "host blocks automated checks - verify by hand")

    def _req(method: str):
        r = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        return urllib.request.urlopen(r, timeout=TIMEOUT)

    for method in (("HEAD",) if fast else ("HEAD", "GET")):
        try:
            with _req(method) as resp:
                code = resp.getcode()
                final = resp.geturl()
                if final.rstrip("/") != url.rstrip("/"):
                    return ("REDIRECT", url, f"{code} -> {final}")
                return ("OK", url, str(code))
        except urllib.error.HTTPError as e:
            # Many servers dislike HEAD but serve GET fine.
            if e.code in (403, 405, 501) and method == "HEAD" and not fast:
                continue
            if e.code in (401, 403):
                return ("SKIP", url, f"HTTP {e.code} (auth/bot wall)")
            return ("DEAD", url, f"HTTP {e.code}")
        except urllib.error.URLError as e:
            return ("DEAD", url, f"{type(e.reason).__name__}: {e.reason}")
        except Exception as e:  # noqa: BLE001
            return ("DEAD", url, f"{type(e).__name__}: {e}")
    return ("DEAD", url, "no response")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="index.html")
    ap.add_argument("--workers", type=int, default=4)  # polite by default; high concurrency causes 429s
    ap.add_argument("--fast", action="store_true")
    args = ap.parse_args()

    urls = extract(args.file)
    if not urls:
        print(f"No URLs found in {args.file}")
        return 0

    hosts = defaultdict(int)
    for u in urls:
        hosts[urlparse(u).netloc] += 1
    print(f"Checking {len(urls)} links across {len(hosts)} hosts in {args.file}\n")

    results: list[tuple[str, str, str]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for i, res in enumerate(ex.map(lambda u: check(u, args.fast), urls), 1):
            results.append(res)
            print(f"\r  checked {i}/{len(urls)}", end="", flush=True)
    print("\r" + " " * 40 + "\r", end="")

    buckets = defaultdict(list)
    for status, url, detail in results:
        buckets[status].append((url, detail))

    for status, label in (("DEAD", "BROKEN — fix these"),
                          ("REDIRECT", "MOVED — consider updating"),
                          ("SKIP", "SKIPPED — could not verify automatically")):
        if buckets[status]:
            print(f"\n{label}  ({len(buckets[status])})")
            for url, detail in sorted(buckets[status]):
                print(f"  {url}\n      {detail}")

    print("\n" + "-" * 58)
    print(f"  OK {len(buckets['OK']):4}   moved {len(buckets['REDIRECT']):3}"
          f"   skipped {len(buckets['SKIP']):3}   BROKEN {len(buckets['DEAD']):3}")
    print("-" * 58)

    if buckets["DEAD"]:
        print("\nBroken links found. A dead link is the fastest way to lose a beginner.")
        return 1
    print("\nNo broken links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
