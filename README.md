> **Play it with Asciiverse.** With [av](https://asciiverse.sh), the Asciiverse
> client:
>
> ```
> av install terminal-pong
> av play terminal-pong
> ```
>
> Or download the archive for your system from this repository's Releases,
> unpack it and run `./terminal-pong` (`terminal-pong.exe` on Windows).
>
> The original README follows.

# Terminal Ping Pong 🏓

A simple, fun ping pong game playable entirely in your terminal. Built with Rust and powered by [`ratatui`](https://crates.io/crates/ratatui) for a beautifully responsive TUI (Text User Interface).

Currently, you can play against a basic AI opponent, a friend locally, or just watch AI vs AI in screensaver mode. It's fast, minimal, and runs right inside your terminal window.

Now with a customizable settings screen: choose your favorite color theme and set default difficulty for each mode!

## 🎥 Demo

<div>
<img src="https://vhs.charm.sh/vhs-6QXgcKWH4C5DJxhDBuVsSq.gif" alt="Gameplay Demo" width="800" height="400" />
</div>

<details>
<summary>🖼️ <b>Settings & Theme Preview</b> (click to expand)</summary>

<img src="https://vhs.charm.sh/vhs-4vwyzEIwT7Z7c1pG0XD8LW.gif" alt="Settings Screen" width="800" height="400" />

</details>

---

## ✨ Features

- 🖥️ Single-player mode vs. computer (AI)
- 👥 Local multiplayer (play with a friend on the same keyboard)
- 🤖 Screensaver mode (AI vs AI, endless pong)
- � Multiple color themes — pick your favorite in the settings
- 🛠️ In-app settings: adjust default difficulty for each mode
- �🎮 Real-time terminal-based gameplay
- � Smooth and colorful UI using `ratatui`
- 🚀 Written in Rust <del>for performance and reliability</del> because I wanted to

---

## 🧑‍💻 Getting Started

### Requirements

- Rust (latest stable recommended)
- A terminal that supports ANSI escape codes

### Installation

git clone [https://github.com/yourusername/terminal-pingpong.git](https://github.com/IshmamR/terminal.pong)

Clone the repository and build:

```bash
git clone https://github.com/IshmamR/terminal.pong.git
cd terminal.pong
cargo run --release
```

Then play directly in your terminal!

### 🎯 Controls

- Up Arrow / Mouse scroll up: Move paddle up
- Down Arrow / Mouse scroll down: Move paddle down
- Space: Power move (for pro players 😉)
- Q: Quit

### 🛠 Tech Stack

- Language: Rust
- UI: ratatui
- Rendering: Crossterm-based backend

---

## 🚧 Roadmap / Planned Features

- [x] 🎮 Local multiplayer support (same terminal)
- [x] 🧠 Computer difficulty levels (adjustable in settings)
- [x] 🌈 Screensaver mode — AI vs AI with endless pong
- [x] 🎨 Theme selection and live preview in settings
- [ ] 💾 Save settings to SQLite database (persistent preferences)
- [ ] 🌐 Network multiplayer (play with a friend remotely)
- [ ] 🏆 High scores / stats

## 📜 License

[MIT](LICENSE).

---

<div align="center">
Made with ❤️ and Rust.
</div>
