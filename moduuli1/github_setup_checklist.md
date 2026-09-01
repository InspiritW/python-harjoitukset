# Module 1-2 checklist: GitHub + version control

You already wrote hello.py. This part has no code — it's just setup steps.
Check each box in your head (or literally edit this file and put an x in the brackets) as you do it.

- [ ] Go to github.com and create a free account (if you don't have one yet)
- [ ] Click "New repository" and create a repo for your Python exercises
      (this repo, python-harjoitukset, might already be it — check)
- [ ] In your terminal, inside this project folder, run: git remote -v
      -> this shows you which GitHub repo your local project is connected to
- [ ] If nothing shows up, connect it with:
      git remote add origin <the URL from your GitHub repo page>
- [ ] Try the three commands you'll use constantly from now on:
      git pull    -> gets any changes from GitHub down to your computer
      git add .   -> stages your changed files
      git commit -m "message"  -> saves a snapshot with a note
      git push    -> sends your snapshot up to GitHub
- [ ] Go check github.com in your browser and confirm your commit shows up there

That's it. Once push/pull/commit work, module 1-2 is done.
