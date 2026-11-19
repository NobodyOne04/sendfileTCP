# sendfileTCP

A 2019 Python exercise: send one file from a client to a server over TCP, with a file-picker
dialog on each side and a size check at the end.

## Run

Python 3 with Tk (`tkinter`), no other dependencies. Both scripts use port 9090.

```sh
python3 "py FileSender/server.py"   # pick where to save the file, then it waits
python3 "py FileSender/client.py"   # pick the file to send
```

## How it works

1. The server binds `:9090`, asks (Tk dialog) for the file to write, and accepts one client.
2. They exchange greetings; the client sends the file size, then the file in 1 KiB chunks.
3. The server writes until it has the announced size (10 s timeout per chunk), then compares
   sizes: on a match it answers "File has load correct"; otherwise it prints the numbers and
   offers to delete the broken file.

The client always connects to `127.0.0.1`, so both sides run on the same machine as written.
It's an archived exercise; for real transfers see
[remote-cmd (tcp-pipe)](https://github.com/NobodyOne04/remote-cmd).

Decisions: [docs/adr](docs/adr/README.md).
