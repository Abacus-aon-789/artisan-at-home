# Artisan at Home — Website Cheat Sheet 🍃

A plain-English guide for editing and running your website yourself.
No code experience needed — just follow the steps.

---

## The 3 tools you use

1. **VS Code** — the editor where you change the website's words and files
   (like Word, but for website files).
2. **Terminal** — runs the little "preview server" so you can see your site
   on your own computer before publishing.
3. **Your browser** — where you view the preview at `localhost:8080`.

---

## The core editing loop (memorise this!)

1. **Open** the file in VS Code (e.g. `index.html` for the homepage).
2. **Change** the words — only edit the text *between* the tags, like
   `<h1>change this bit</h1>`. Leave the `<...>` "bookends" alone.
3. **Save** with **Cmd + S**.
4. **Refresh** the preview with **Cmd + Shift + R** (the "hard refresh").

That's it. Every edit is a version of these 4 steps.

> ⚠️ Always use **Cmd + Shift + R**, not a normal refresh. A plain refresh
> often shows you an old, cached copy and makes you think nothing changed.

---

## Starting the preview (if localhost:8080 isn't working)

The preview only runs while the Terminal server is on. To start it:

1. Open **Terminal**.
2. Paste this and press Enter:

   ```
   cd /Users/AbiGlover/Documents/ArtisanWebsite
   ```

3. Paste this and press Enter:

   ```
   python3 -m http.server 8080
   ```

4. Leave that Terminal window open, and go to **http://localhost:8080**
   in your browser.

> That Terminal window is "busy" running the server — it won't let you type
> other commands. To run something else, open a **new** Terminal window
> with **Cmd + N**.

---

## Finding things in a file

- In VS Code, press **Cmd + F** to search within the open file.
- To search across ALL files at once, press **Cmd + Shift + F**.

---

## Where the pages live

- `index.html` (top level) = **Homepage**
- `our-story/index.html` = Our Story page
- `contact-us/index.html` = Contact page
- `faqs/index.html` = FAQs page
- `services/` folder = the individual service pages
- `images/` folder = all your photos
- `css/styles.css` = controls colours, fonts, and layout (advanced — careful here)

---

## Publishing changes (making them go live)

Editing a file only changes your computer's copy. To put a change on the
real internet, it has to reach **GitHub**, and Vercel then publishes it
automatically (~1 minute). Since GitHub Desktop won't run on your Mac, use
the browser. Two cases:

**A. Changing an existing page** (e.g. fixing wording):

1. Make + save the edit in VS Code (so your copy stays correct)
2. Go to github.com → your `artisan-at-home` repo
3. Click into the file (e.g. `contact-us` → `index.html`)
4. Click the **pencil** ✏️ ("Edit this file")
5. Make the same change there (or select-all and paste your VS Code version)
6. Green **Commit changes…** → **Commit changes**

**B. Adding a brand-new page/file:**

1. In the repo, click **Add file → Create new file**
2. Type the path, e.g. `new-page/index.html` (the `/` makes the folder)
3. In VS Code, open your local file, **Cmd+A**, **Cmd+C**
4. Paste into GitHub's editor, then **Commit changes**

> Avoid drag-and-dropping folders into GitHub — it silently misses files.
> Copy-paste is reliable.

After committing, wait ~1 min, then hard-refresh the live site to check.

---

## Local vs. Live — the big distinction

- **localhost:8080** = your PRIVATE preview, only on your computer. Edit here
  freely; nobody else sees it.
- **The public internet** = only updates when you deliberately **publish**.

Your edits are NOT live to the world until you publish them (via Vercel).

---

## Golden rules for peace of mind

- You can't break the real website by editing on your computer.
- If an edit looks wrong, you can always undo in VS Code with **Cmd + Z**.
- When in doubt, save, hard-refresh, and look at the preview.
- Ask Claude anytime — describe what you see and we'll sort it.

---

*Made with Claude. Keep this file in your ArtisanWebsite folder for reference.*
