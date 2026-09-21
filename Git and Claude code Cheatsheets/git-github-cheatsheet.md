# Git & GitHub Cheatsheet

> Full markdown transcription of `git-github-cheatsheet.html` (same content, plain markdown so it reads directly on GitHub).

## ⚙ Setup

```bash
git config --global user.name "তোমার নাম"
```
Git username set করো

```bash
git config --global user.email "email@gmail.com"
```
Git email set করো

```bash
git config --list
```
সব configuration দেখো

---

## 🌱 Repo Start

```bash
git init
```
নতুন Git repository তৈরি করো

```bash
git clone https://github.com/user/repo
```
GitHub repo copy করো

```bash
git status
```
কি change হয়েছে দেখো

```bash
git log --oneline
```
সব commit history দেখো

---

## 📦 Add & Commit

```bash
git add .
```
সব files stage করো

```bash
git add filename.py
```
একটা file stage করো

```bash
git commit -m "fix navbar"
```
changes save করো

```bash
git commit --amend
```
শেষ commit edit করো

---

## ☁ Push & Pull

```bash
git push
```
GitHub এ upload করো

```bash
git pull
```
latest changes নামাও

```bash
git fetch
```
changes check করো

```bash
git push -u origin main
```
প্রথম push এর সময়

---

## 🌿 Branching

```bash
git branch
```
সব branch দেখো

```bash
git checkout new-feature
```
branch change করো

```bash
git checkout -b new-feature
```
নতুন branch তৈরি + switch

```bash
git merge new-feature
```
branch merge করো

---

## ↩ Undo / Fix

```bash
git restore .
```
সব unstaged changes remove

```bash
git reset HEAD~1
```
শেষ commit undo

```bash
git stash
```
temporary save

```bash
git stash pop
```
stash ফিরিয়ে আনো

---

## 🔗 GitHub Connect

```bash
git remote add origin https://github.com/user/repo.git
```
GitHub repo connect করো

```bash
git remote -v
```
connected remote দেখো

```bash
git branch -M main
```
main branch rename করো

```bash
git push -u origin main
```
GitHub এ প্রথম push

---

## 🐙 GitHub CLI

```bash
gh auth login
```
GitHub login

```bash
gh repo create
```
নতুন repo তৈরি

```bash
gh repo clone user/repo
```
repo clone

```bash
gh repo view
```
repo details দেখো

---

## 🔀 Pull Requests

```bash
gh pr create
```
নতুন Pull Request তৈরি

```bash
gh pr list
```
সব PR দেখো

```bash
gh pr checkout 12
```
PR locally checkout করো

---

> 💡 💡 এটা একবার করলেই সব project এ কাজ করবে

> 💡 💡 Pull Request team collaboration এর সবচেয়ে গুরুত্বপূর্ণ অংশ
