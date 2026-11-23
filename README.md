# One Word From Grandma

[![Competition](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![Rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![Reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)

Entry for the make.fun bounty
[One Word From Grandma](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
($5, closes 27 Nov 2026 02:05 WIB).

## The word

**Robbie** — six letters, one word, no spaces, no punctuation.

Grandma has named her robot — the way she would name a grandson.
Warm, a little confused, funny in a single word, and unmistakably
about a machine she has adopted into the family. One word, no caption
needed.

## How it works

`main.py` (Python stdlib only, deterministic, no network) writes the
word to `/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt`
when that environment variable is set.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # Robbie
```

## License

MIT — see [LICENSE](LICENSE).
