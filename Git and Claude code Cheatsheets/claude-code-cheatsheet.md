# Claude Code CLI Cheatsheet

> Full markdown transcription of `claude-code-cheatsheet.html` (same content, plain markdown so it reads directly on GitHub).

## 🚀 Start & Launch

```bash
claude
```
নতুন session শুরু করো (current folder এ)

```bash
claude --continue
```
আগের সর্বশেষ session continue করো

```bash
claude -c
```
--continue এর shortcut

```bash
claude --resume
```
পুরনো conversations এর list দেখাবে, বেছে নাও

---

## 📁 Folder Navigation (CMD)

```bash
cd FolderName
```
কোনো folder এ ঢোকো

```bash
cd ..
```
এক ধাপ পিছনে যাও

```bash
cd C:\Users\User\Documents
```
সরাসরি full path দিয়ে যাও

```bash
dir
```
বর্তমান folder এর সব files দেখো

---

## ⚡ Quick / One-off Commands

```bash
claude "তোমার প্রশ্ন এখানে"
```
session না খুলেই সরাসরি প্রশ্ন করো

```bash
claude -p "fix bug in app.py"
```
--print shortcut, output terminal এ দেখাবে

```bash
claude --version
```
installed version চেক করো

```bash
claude doctor
```
installation ঠিকঠাক আছে কিনা চেক করো

---

## 💬 Inside Session — Slash Commands

*(see the **Slash Commands** table at the end of this file)*

---

## 🔐 Login & Auth

```bash
claude
```
প্রথমবার চালালে browser এ login হবে automatically

```bash
claude logout
```
logout করো

```bash
claude login
```
আবার login করো

---

## 💡 Pro Tips

- **[TIP]** সবসময় project folder এ গিয়ে claude চালাও, তাহলে Claude তোমার files দেখতে পাবে।
- **[TIP]** Install এর পর CMD বন্ধ করে নতুন করে খোলো — না হলে claude command কাজ নাও করতে পারে।
- **[TIP]** Windows Terminal app ব্যবহার করলে output সুন্দর দেখায়। Microsoft Store থেকে free নামাও।
- **[NOTE]** কোনো সমস্যা হলে claude doctor চালাও — বেশিরভাগ সমস্যা ধরে দেবে।

---

## 🔧 Advanced Usage

```bash
claude -p "review app.py" > result.txt
```
Claude এর output একটা file এ save করো

```bash
claude --model claude-opus-4-5
```
নির্দিষ্ট model দিয়ে চালাও

```bash
claude --help
```
সব available flags ও options দেখো

```bash
exit
```
CMD window বন্ধ করো

---

## 🔄 Daily Workflow

1. CMD / PowerShell খোলো
2. `cd তোমার-project-folder` — project folder এ যাও
3. `claude -c` — আগের session থেকে continue করো অথবা নতুন শুরু করো
4. কাজ শেষে /exit বা CMD এর X চাপো

---

## Slash Commands

| Command | What it does |
|---|---|
| `/help` | সব command দেখো |
| `/exit` | session বন্ধ করো |
| `/clear` | chat history মুছো |
| `/status` | account info দেখো |
| `/model` | AI model বদলাও |
| `/cost` | কত টাকা খরচ হলো |
