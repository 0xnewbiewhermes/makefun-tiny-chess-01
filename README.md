# makefun-tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/0xnewbiewhermes/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/0xnewbiewhermes/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An original chess engine in 4,078 bytes of Python (standard library only). 10x12 mailbox board stored as a string, flipped and case-swapped each ply so the side to move is always uppercase; pseudo-legal move generation with a king-capture legality model; iterative-deepening negamax with alpha-beta pruning, a transposition table, null-window root search, MVV-LVA move ordering, and a capture-only quiescence search. Evaluation is material plus hand-authored piece-square tables maintained incrementally, and the root is repetition-aware across the game. The search runs to a fixed node budget per move, so play is fully deterministic and replayable.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8732 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=17fk2ks1&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
