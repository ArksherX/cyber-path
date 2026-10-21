# Cyber Path

**A self-study map of cybersecurity careers. One page, twenty paths, no sign-up.**

Everyone starts at Foundations. Then you pick one of seven domains — Offensive,
Defensive/SOC, Threat Intel & DFIR, DevSecOps, AI Security, GRC, or Security
Engineering & Cloud — and work through Level 2 and Level 3 paths. Every week tells you
what to open, what to build, and how to know you're done.

> **▶ Start here: https://ARKSHERX.github.io/cyber-path/**
> *(replace with your actual Pages URL once enabled — see Setup below)*

---

## What's in it

| | |
|---|---|
| **20** | learning paths |
| **170** | weeks of structured study |
| **497** | individual steps |
| **139** | checked links to free and paid resources |
| **7** | domains, plus a shared Foundations track |

Plus a **role quiz** if you don't know which domain fits, a **study planner**, a
**weekly log**, and **progress tracking** that ticks off steps as you finish them.

## Three things that make it practical

**It works completely offline.** There are no external scripts, no trackers, no API
calls — the entire thing is one self-contained HTML file. Download it once and it works
on a plane, on mobile data you're rationing, or on a connection that drops. That is
deliberate.

**No account, no email, nothing to sign up for.** Your progress is stored in your own
browser, on your own device. Nobody is collecting it, because there's no server to
collect it with.

**It's one file.** Easy to share on WhatsApp, drop on a USB stick, or hand to a study
group that doesn't all have reliable internet.

---

## How to use it

### Option 1 — just open it (easiest)
Visit the link above. That's it. Works on phone and desktop.

### Option 2 — download and keep it
Download `index.html`, open it in any browser. Works with no internet connection.

```bash
# or grab it from the command line
curl -L -o cyber-path.html https://raw.githubusercontent.com/ARKSHERX/cyber-path/main/index.html
```

### Option 3 — clone it
```bash
git clone https://github.com/ARKSHERX/cyber-path.git
cd cyber-path
# open index.html in your browser
```

---

## ⚠️ Important: how your progress is saved

Your progress is saved **in the browser you're using, on the device you're using.**
It is not synced anywhere.

That means:
- Progress on the **website** and progress on a **downloaded copy** are stored separately.
- Clearing your browser data will erase it.
- A different device or browser starts fresh.

**So use the built-in Backup and restore.** Open *Backup and restore* in the sidebar,
export your progress to a file, and keep it. You can restore it on any device, or after
clearing your browser. If you're switching between the hosted version and a downloaded
copy, this is how you carry your progress across.

---

## Contributing

Corrections and additions are genuinely welcome — especially:
- **Broken links.** 139 external links will rot over time. Reporting a dead one is the
  single most useful contribution.
- **Better free resources**, particularly ones accessible outside the US/EU.
- **Corrections** to anything outdated or wrong.

Open an issue, or send a pull request against `index.html`.

**Please don't** send pull requests that add paid courses you're affiliated with, or
that replace free resources with gated ones. The point is that someone with no money
and a slow connection can still learn this.

---

## Licence

**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)** — Creative Commons
Attribution-ShareAlike.

You can share it, adapt it, translate it, print it, or teach from it — including
commercially. Two conditions: **credit the original**, and **keep derivatives under the
same licence** so they stay open too.

Translations are especially welcome. If you translate it, open an issue so it can be
linked from here.

Linked third-party resources belong to their respective owners and carry their own terms.

---

## Setup (for the maintainer)

To publish this with GitHub Pages:

1. Create the repo and push (see `SETUP.md`).
2. On GitHub: **Settings → Pages → Source: Deploy from a branch → `main` / `(root)` → Save.**
3. Wait ~1 minute. The URL appears on that same settings page.
4. Update the link at the top of this README.

GitHub Pages is free for public repositories.

---

Built by [Miracle Owolabi](https://www.linkedin.com/in/miracleowolabi-security).
If it helped you, pass it on to someone starting out.
