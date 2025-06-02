# ⚡ Universal Terminal Downloader (Python But Is Terminal Base :P)

A fast, lightweight, terminal-based downloader like IDM — built in pure Python.

✅ Cross-platform (Windows, Linux, macOS)  
✅ No external libraries required  
✅ Pause, Resume, Cancel  
✅ Multi-threaded for **maximum speed**  
✅ Emoji support fallback for old terminals  
✅ Bypasses system proxy (e.g. Nekoray)

---

## 📦 Features

- 🔄 **Pause** / **Resume** / **Cancel** with keypress
- 🚀 Multi-threaded download (default: 8 threads)
- 🧠 Efficient CPU & RAM usage
- 🛑 Cancel waits 10s then auto exits
- 🔥 Pure Python — no dependencies
- 🎭 Emoji fallback for older terminals
- 🌐 Ignores system proxy for VPN bypass

---

## 📥 How to Use

1. **Run the script**:

   ```bash
   python universal_downloader.py
   ```
   
2. **Paste the download URL**

3. While downloading, press:

   * `P` → Pause
   * `R` → Resume
   * `C` → Cancel (auto-exits after 10s)

---

## 🧪 Example Output

```
[===========       ] {  65/100 }%  [P]ause [R]esume [C]ancel 
```

---

## 🧰 Requirements

* Python 3.6+
* No extra libraries — uses only built-in Python

---

## 📁 Output Location

Downloads are saved to:

* `F:/downloads` (on Windows)
* `~/downloads` (on Linux/macOS)

---

## ⚙️ Configuration

To change:

```python
NUM_THREADS = 8
DOWNLOAD_DIR = "F:/downloads"
```

---

## 🛡 Proxy Bypass

This script bypasses any system-level proxy (e.g. Nekoray/V2Ray) to download directly from your main IP.

---

## 📌 License

Free to use, modify, and share — no credit required.

---

## 🧠 TODO Ideas

* Resume after app restart
* GUI version (PyQt/Tkinter)
* Multi-file `.txt` downloader
* Speed limiter option
* Retry on connection fail

---
### Creators And Pull Request :-)
 create by Vortex Team
* But 
 if you a programmer and if you need to help me and my team pull request then on readme please write english and full change 

