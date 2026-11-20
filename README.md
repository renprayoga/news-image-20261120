# The World in One Image — Friday 20 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![The World in One Image](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)

A one-page newspaper front page that sums up Friday 20 November 2026 in a
single 1024×1024 image. Every icon is drawn from scratch with Pillow
geometry — no photos, no copied artwork.

## The stories

1. **Myanmar guilty of Rohingya genocide (hero).** On Thursday 19 November
   the International Court of Justice in The Hague ruled 9–6 that Myanmar
   committed genocide against the Rohingya — the first time in the court's
   80-year history that a state has been held responsible for genocide.
   Around 10,000 Rohingya were killed in the 2017 "clearance operations" in
   Rakhine; the court ordered reparations and a report within two years.
   The case was brought by The Gambia in 2019.
2. **Trump: no new Iran strikes before 2027.** Speaking to reporters aboard
   Air Force One on his way back from China on 19 November, President Trump
   said he was "not rushing into any decision" and that "we'll see what
   happens after the beginning of the year". Israel is pressing for new
   strikes; the decision is pushed to next year.
3. **Cyclone Akvan hits Odisha today.** The severe cyclone made landfall
   near Gopalpur, Odisha, around midday IST on Friday 20 November, with
   winds of 90–100 km/h and gusts to 110. 105,304 people were evacuated to
   1,224 shelters; the state aims for zero casualties, with a red alert in
   11 districts.
4. **GTA 6 sales pass $1.8 billion.** Launch-week sales of Grand Theft Auto
   VI — released worldwide on 19 November for PS5 and Xbox — have passed
   $1.80 billion, more than the global box office of the film The Odyssey.

**Also:** a Houthi strike hit Riyadh, damaging the Saudi PIF tower; Russian
strikes damaged the Austrian and Dutch embassies in Kyiv; Europe is ready to
talk to Russia about ending the war in Ukraine.

## How it works

- `draw.py` — deterministic Pillow renderer. It draws the whole front page
  (masthead, date bar, navy hero panel with hand-drawn scales of justice,
  three story rows with geometric icons, ALSO strip, sources footer) from
  fixed constants. No network, no randomness, no timestamps.
- `main.py` — standard library only. It copies `entry.png` byte for byte
  into `$MAKEFUN_OUTPUT_DIR` (default `./output/`) as `entry.png`. Two runs
  write identical bytes.
- `entry.png` — the rendered 1024×1024 image (≤ 1 MiB).

## Run it

```sh
python3 draw.py            # re-render entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # write out/entry.png
```

## Sources

CNN, Le Monde, Reuters, Axios, IMD, The Hindu, BBC.

## License

MIT — see `LICENSE`.
