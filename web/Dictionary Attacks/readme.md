# Multithreaded Dictionary Attack Script

This script performs a **multithreaded dictionary attack** against a target HTTP endpoint.
It is designed for educational purposes based on **Hack The Box Academy Module** — see link below.

## 📘 Hack The Box Academy Reference

🔗 **Module Link:** [https://academy.hackthebox.com/module/57/section/487](https://academy.hackthebox.com/module/57/section/487)

*(Note: Requires Hack The Box Academy access to view)*

## 🔎 Description

The script:

* Downloads a list of common passwords from SecLists
* Sends concurrent HTTP POST requests to `/dictionary`
* Uses multithreading (`ThreadPoolExecutor`) for improved speed
* Displays progress with a `tqdm` progress bar
* Stops as soon as a valid password (with flag) is found

## ⚙️ Requirements

* Python 3.8+
* `requests`
* `tqdm`

Install dependencies:

```bash
pip install requests tqdm
```

## 🚀 Usage

1. Update target host & port:

```python
ip = "127.0.0.1"
port = 1234
```

2. Run:

```bash
python3 script.py
```

## 📌 How It Works

* Downloads password list from SecLists
* Tries each password via HTTP POST
* Uses 50 threads for concurrency
* Stops when correct password (flag) is found

## 🛡 Disclaimer

For **educational / authorized testing only**.
Do not run against systems without permission.
