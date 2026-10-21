# Publishing this repo

One-time setup. Replace `cyber-path` if you want a different repo name.

## 1. Create the repo and push

With the GitHub CLI (easiest — it creates the repo and pushes in one step):

```bash
cd ~/CyberPath
git init
git add -A
git commit -m "Cyber Path: a self-study map of cybersecurity careers"
git branch -M main
gh repo create cyber-path --public --source=. --remote=origin --push \
  --description "A self-study map of cybersecurity careers. 20 paths, 170 weeks, works offline."
```

Without the CLI: create an empty public repo named `cyber-path` on github.com, then:

```bash
cd ~/CyberPath
git init && git add -A
git commit -m "Cyber Path: a self-study map of cybersecurity careers"
git branch -M main
git remote add origin https://github.com/<your-username>/cyber-path.git
git push -u origin main
```

## 2. Turn on GitHub Pages — this is the important step

**Settings → Pages → Source: "Deploy from a branch" → Branch: `main`, folder: `/ (root)` → Save**

Wait about a minute. Your URL will be:

```
https://<your-username>.github.io/cyber-path/
```

Then update the link at the top of `README.md` and push again.

### Why Pages matters
Without it, clicking `index.html` on GitHub shows **raw HTML source**, not the page.
A learner would have to find "Raw", save the file, then open it — three steps most
people won't take. With Pages, it's one link that works on a phone.

## 3. Make it findable

On the repo page, click the gear next to **About** and add topics:

```
cybersecurity  infosec  learning-resources  career-development  study-guide
soc-analyst  penetration-testing  devsecops  grc  ai-security  free-resources
```

Topics are how people actually discover repos like this.

## 4. Updating it later

```bash
cd ~/CyberPath
cp "/home/arksher/Desktop/Cyber Path.html" index.html   # if you edit the original
git add -A && git commit -m "Update: <what changed>"
git push
```

Pages redeploys automatically within a minute.

> **Keep the filename `index.html`.** Renaming it breaks Pages.

## 5. Worth doing eventually

- **Check for dead links.** 139 external links will rot. Run a checker every few months:
  ```bash
  # one option, no install needed if you have npx
  npx linkinator ./index.html --skip "localhost"
  ```
- **Add a CHANGELOG** once people depend on it, so returning learners can see what's new.
- **Watch the issues tab.** The first contributor experience decides whether there's a second.
