# sendfileTCP

A 2019 Python exercise: client sends a file to a server over TCP, Tk file dialogs on both sides.

## Commands
- `python3 "py FileSender/server.py"`, then `python3 "py FileSender/client.py"` (port 9090,
  Python 3 with tkinter, no other dependencies). No tests.

## Layout
- `py FileSender/server.py`: receives and size-checks the file.
- `py FileSender/client.py`: picks and sends the file, prints server messages in a thread.
- `docs/adr/`: decision records (`.adr`), index in `docs/adr/README.md`.

## Conventions
- Read the ADR before changing a recorded decision; commit subjects carry its number.
- The folder name has a space: quote paths.
- Archived exercise: docs or small fixes only unless asked.
