#!/usr/bin/env python3
"""Records asciiverse/terminal-pong.cast, the catalog preview, at 100x30
(hub/RECORDING.md): the title menu, then "I like to watch" (AI against
AI) for about 25 s, then Esc and q to quit. Usage, from the repo root
with a release build: python3 asciiverse/record-preview.py [binary]"""
import os, pty, struct, fcntl, select, sys, termios, time

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
binary = sys.argv[1] if len(sys.argv) > 1 else f"{root}/target/release/terminal-pong"
env = dict(os.environ, TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8")
DOWN = b"\x1b[B"
keys = [(3.0, DOWN), (0.6, DOWN), (0.8, b"\r"), (25.0, b"\x1b"), (1.5, b"q"), (1.5, b"")]

pid, fd = pty.fork()
if pid == 0:
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q", "-i", "2",
        "--capture-env", "TERM,COLORTERM,LANG", "-c", binary,
        f"{root}/asciiverse/terminal-pong.cast"], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 30, 100, 0, 0))
for wait, key in keys:
    end = time.time() + wait
    while time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.03)
        if r:
            try: os.read(fd, 65536)
            except OSError: break
    if key: os.write(fd, key)
for _ in range(50):
    if os.waitpid(pid, os.WNOHANG)[0]: break
    time.sleep(0.2)
