# 🔐 HTB Academy – PIN Brute Force Script

This repository contains a multithreaded Python script created for the following Hack The Box Academy challenge:

🔗 [https://academy.hackthebox.com/module/57/section/498](https://academy.hackthebox.com/module/57/section/498)

The challenge requires brute-forcing a 4-digit PIN via an HTTP endpoint to retrieve the flag.

---

## 🧩 Challenge Overview

The target application validates a PIN using:

```
http://TARGET_IP:PORT/pin?pin=XXXX
```

The goal is to discover the correct 4-digit PIN (`0000–9999`) that returns a JSON response containing the flag.

---

## 🚀 Usage

1. Edit the target IP and port inside the script.
2. Run:

```bash
python3 bruteforcer.py
```

The script automatically stops when the correct PIN is found.

---

## 📦 Requirements

* Python 3
* requests
* tqdm

Install dependencies:

```bash
pip install requests tqdm
```

---

## ⚠️ Disclaimer

This script is for educational purposes only and should be used strictly in authorized environments such as Hack The Box Academy.
