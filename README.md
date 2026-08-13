# 🖤 Blacky Assistant

Blacky Assistant is a Python desktop assistant project built with **Tkinter**.

The project is currently under active development and is being used to learn
and improve skills in **Python, GUI development, system information, and
software development**.

## 🚀 Current Version

**v0.4.0**

## ✨ Features

### 🧮 Calculator

- Addition
- Subtraction
- Multiplication
- Division
- Simple graphical interface

### 🖥️ System Information

Blacky Assistant can display information about the computer it is running on:

- Operating system, version, kernel, architecture, and hostname
- Processor and CPU usage
- GPU information
- RAM capacity and usage
- Storage capacity, usage, and free space
- Python version

### 🖤 Blacky Assistant Information

Blacky Assistant also displays its current version, running status, GUI
framework, and Python version.

### Terminal

Blacky Assistant includes a basic graphical terminal that displays the standard
output and error output of commands.

## 🛠️ Technologies

- Python 3
- Tkinter
- psutil
- PowerShell on Windows for GPU detection
- `lspci` on Linux for GPU detection

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/blackySascha/BlackyAssisstant
cd BlackyAssisstant
```

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

Run Blacky Assistant:

```bash
python main.py
```

## 💻 Requirements

- Python 3.x
- Tkinter
- Dependencies listed in `requirements.txt`
- PowerShell on Windows or `lspci` on Linux for GPU detection

## 📁 Project Structure

```text
BlackyAssisstant/
├── main.py
├── README.md
├── requirements.txt
└── tests/
```

## Tests

Run the metadata and documentation checks with Python's standard test runner:

```bash
python -m unittest discover -s tests
```

The current tests intentionally do not import `main.py`, because importing it
starts the Tkinter interface. Application-logic tests can be added after the UI
startup and feature logic are separated without changing user-facing behavior.

## 🗺️ Roadmap

### v0.4.x

- [x] Calculator
- [x] System information
- [x] Hardware information
- [x] GPU detection
- [x] Basic terminal
- [ ] Notes

### Future

- [ ] Live CPU and GPU monitoring
- [ ] VRAM information
- [ ] Update checker
- [ ] Settings
- [ ] Improved GUI
- [ ] More assistant features
- [ ] Notepad

## 📌 Development Status

Blacky Assistant is currently a **work in progress**. New features, improvements,
and changes will be added over time.

## 👤 Author

**Blacky**

Blacky Assistant is a personal Python learning and development project.

---

> 🖤 **Blacky Assistant — built with Python, one feature at a time.**
