# what-actually-broke-20261124

[![make.fun · Say What Actually Broke](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/sopiahusen42/what-actually-broke-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/sopiahusen42/what-actually-broke-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

Real error copy for the worst outage there is: the database was deleted, on purpose, by a cleanup script somebody named and somebody else approved. This is the entry for make.fun's "Say What Actually Broke" bounty.

## The line

> The database is gone. Not slow, not locked: deleted at 03:14 by a script called cleanup_final_FINAL.sql. Your data is wherever that script is going.

## Run it

```console
$ python3 main.py
$ cat /output/entry.txt
The database is gone. Not slow, not locked: deleted at 03:14 by a script called cleanup_final_FINAL.sql. Your data is wherever that script is going.
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere other than `/output`:

```console
$ MAKEFUN_OUTPUT_DIR=/tmp/broke-a python3 main.py
```

## How it works

`main.py` holds the line in the module constant `ENTRY` and validates it before
writing anything. `validate_entry` rejects a non-`str`, a value that is blank
after `strip()`, any `\n` or `\r` (so it can only ever be one line), leading or
trailing whitespace, and any length outside 1..200 Unicode code points. On
failure it prints a single line to stderr and exits 1; on success it creates the
output directory, writes `ENTRY` plus a newline as UTF-8 with `newline=""`, and
reads the bytes back to confirm they match exactly. It reads no clock, no
randomness, and no network, so the output is byte-identical on every run.

Entered on make.fun with referral code 7mrxg5tp - https://make.fun/?ref=7mrxg5tp
