# Changes from upstream

This is the Asciiverse packaging of [terminal.pong](https://github.com/IshmamR/terminal.pong)
by IshmamR (MIT), built from upstream's master as of July 2025 (version
0.1.0; upstream has no tags). Upstream is the `upstream` remote; the
`asciiverse` branch carries the changes below. Both are worth offering
upstream.

## Code

- **The court follows the window size.** It was a fixed 130x28 box and the
  game refused smaller windows. It now fills the window down to 70x20, and
  resizing while playing keeps the paddles and the ball inside the court.
  A new game also starts centred (it used to get an empty area until its
  first frame, which put everything in the top-left corner). The title
  bar and the controls line fit the width.
- **Draws at the game's frame rate.** The game loop returned at once when
  the next physics frame was not due, so the screen was redrawn thousands
  of times a second: 81% of a core while watching. It now sleeps out the
  rest of each frame (15 to 40 per second, by difficulty): about 1%.

## Packaging (new files)

- `.github/workflows/release.yml`: av archives for Linux (static), macOS
  and Windows, each x86-64 and ARM64, plus SHA256SUMS, and .deb, .rpm,
  .apk and Arch packages.
- `asciiverse/nfpm.yaml`: the system packages.
- `asciiverse/record-preview.py`: records the catalog preview (the menu,
  then "I like to watch").
