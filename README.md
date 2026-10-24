# Blacky Assistant

A personal Python learning project with a Tkinter desktop interface: a calculator,
local system information and a basic command runner.

**Status:** early prototype. The displayed application version is **v0.4.0**.
There are no published releases. This is not a production-ready assistant.

## Functionality

| Component | Current implementation |
| --- | --- |
| Calculator | Addition, subtraction, multiplication and division of two integer inputs. Division may return a decimal result. |
| System information | OS, Python version, hostname, processor, CPU usage, memory and disk usage. Values are collected when the view opens. |
| GPU information | Queries PowerShell on Windows or `lspci` on Linux. Other systems return `Unknown`. |
| Command runner | Runs a local shell command and displays standard output and error output after it finishes. |
| Notes | Placeholder only; no editor or saved notes. |

## Requirements

- Python 3 with Tkinter and a graphical desktop session.
- `psutil`, as declared in `requirements.txt`.
- For GPU detection: PowerShell on Windows; Bash, `lspci` and `grep` on Linux.

Tkinter may require a separate operating-system package on Linux. GPU detection
is platform-specific; compatibility with every operating system is not claimed.

## Installation and launch

```sh
git clone https://github.com/alexschwarz-dev/BlackyAssistant.git
cd BlackyAssistant
```

Create a virtual environment and use its Python executable directly. Activation
is not required for these commands.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

### Linux

```sh
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python main.py
```

## Usage and limitations

Select **Start Blacky Assistant**, then choose a component. Closing a calculator
or information window does not restore the menu buttons automatically; use
**Home** in the main window to rebuild the menu.

- The calculator does not yet handle invalid input or division by zero in the UI.
- System values are snapshots, not continuous monitoring.
- Commands run synchronously, so a long-running command can block the interface.
- The command runner is not an interactive terminal: interactive input and a
  persistent shell session are not implemented.
- Commands execute with the current user's permissions via `shell=True`. They
  can modify files and run programs. Only enter commands you understand and trust.
- Hostnames and command output may contain personal information. Check them
  before sharing screenshots or logs.

## Repository structure

```text
BlackyAssistant/
|-- main.py                       # Interface and application logic
|-- requirements.txt              # Third-party runtime dependency
|-- README.md
|-- .gitattributes
|-- .gitignore
`-- tests/
    `-- test_project_metadata.py  # Setup and documentation checks
```

## Checks

Using the virtual environment's Python executable, run:

```sh
python -m unittest discover -s tests
python -m py_compile main.py
```

Replace `python` with `.\\.venv\\Scripts\\python.exe` on Windows or
`./.venv/bin/python` on Linux when the environment is not activated.
The existing tests cover project metadata only. They do not establish GUI
correctness, calculator correctness or cross-platform compatibility. Importing
`main.py` currently starts the interface, so the tests do not import it.

## Possible next steps

- Separate interface startup from application logic to make behavior testable.
- Add calculator input validation and clearer error messages.
- Keep navigation available while component windows are open.
- Run commands without blocking the interface and define cancellation behavior.
- Implement a notes editor before presenting Notes as an available feature.

These are development ideas, not completed features or delivery commitments.
