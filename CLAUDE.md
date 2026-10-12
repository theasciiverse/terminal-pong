# terminal.pong (Asciiverse packaging)

Pong in the terminal, by IshmamR, in Rust and Ratatui; packaged for the
Asciiverse catalog and as system packages. Not our code: keep changes
small, list every one in PATCHES.md, and offer fixes upstream.

- Remotes: `upstream` is github.com/IshmamR/terminal.pong, `origin` is
  github.com/theasciiverse/terminal-pong.
- Branch `asciiverse` = upstream master plus our commits.
- Release: tag `v<version>-av.<n>` and push it.
- Local static build: `docker run --rm -v "$PWD":/src -w /src
  rust:1-alpine sh -c 'apk add musl-dev && cargo build --release'`.
- Settings live in memory only; nothing is written to disk.
