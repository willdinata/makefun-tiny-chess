# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/willdinata/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/willdinata/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01/reward?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine that fits in under 4 KB of Python. It keeps the board on a 0x88 array and searches with negamax alpha-beta: a transposition table, quiescence over captures and promotions (every evasion when in check), check extensions, late move reductions, and MVV-LVA plus killer and history move ordering. The evaluation is material plus piece-square tables whose king table blends toward an endgame table as pieces come off, with in-search repetition and the fifty-move rule scored as draws. It thinks for a fixed budget of 60,000 nodes per move and never reads a clock, so a trial replays move for move.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 main.py
```

It plays every game the env at MAKEFUN_ENV_URL serves, answering each of its positions with the move the search picks, until the env reports the gauntlet done.

---

<sub>Entered on [make.fun](https://make.fun/?ref=63p7zf8z&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
