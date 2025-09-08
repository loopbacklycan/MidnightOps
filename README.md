# 🕶️ MidnightOps – Subdomain Enumerator

> _“Scan in silence. Strike in the dark.”_

MidnightOps is a fast, threaded subdomain enumeration tool written in Python. Designed for security researchers, bug bounty hunters, and digital ninjas who move under the cover of terminal shadows.

![Banner](https://github.com/loopbacklycan/MidnightOps/blob/main/banner.png)  
> *Banner ASCII art included by default. No external dependencies required.*

---

## ⚙️ Features

- 🧠 Simple, fast, threaded subdomain enumeration  
- 📂 Uses a customizable wordlist (`wordlists/subdomains.txt`)  
- 💾 Saves results to `output/found_subdomains.txt`  
- 🖼️ Built-in ASCII banner because style matters  
- 💻 No external dependencies — runs on raw Python 3  

---

## 🚀 Usage

```bash
git clone https://github.com/loopbacklycan/MidnightOps.git
cd MidnightOps
python3 midnightops.py
