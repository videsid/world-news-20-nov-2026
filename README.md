# Sum up 20 November's world news in one image

Entry for the make.fun bounty **"Sum up 20 November's world news in one image"**
($250, 50 paid places), deadline Sunday 22 November 2026, 07:00 WIB.

## The image

`image.jpg` — one square image, 1024×1024 px, ~363 KB (limit: 1 MiB).
Newspaper-front-page style, six labelled panels plus a small strip:

1. **Kyiv under fire** — Russia's overnight missile and drone strike hit
   bridges over the Dnipro; 8 killed, 28 injured across nine regions.
2. **Poland airspace breach** — Russian missiles and a drone crossed into
   Poland; Chancellor Merz warned Europe will not accept a Yalta-style
   settlement negotiated without Europeans.
3. **Iran war: no decision yet** — Trump delays the Iran decision to the
   new year; the Senate blocks a war vote 51–48; tanker attacks in the
   Strait of Hormuz intensify.
4. **Houthi missiles hit Riyadh** — missiles struck Riyadh's financial
   district, damaging the PIF tower; Saudi air defences intercepted more.
5. **COP31 deadlocked** — the final-day Antalya draft drops fossil fuels
   entirely; Panama threatened a veto; no deal agreed.
6. **GTA VI smashes records** — official first-24-hours sales of
   $3.79 billion, 32.5 million units, Metacritic 99 — the biggest
   entertainment launch in history.

Small strip: UK expelling Myanmar's defence attaché after the ICJ ruling,
Kenya discharging its last Ebola patient, Iraqi federal forces deploying
near Jurf al-Sakhar, and Haiti police reporting 34 suspected gang members
killed.

Facts were checked against secondary/aggregator summaries (Just Security,
OneTurn, Open Chronicle, UN News, and Reuters/CNN/Barron's on GTA VI) on
the morning of 21 November 2026.

## How to run

```sh
python3 main.py   # writes output.jpg, byte-identical to image.jpg
```

No network access, no dependencies beyond the Python 3.13 standard
library. Running it twice writes the same bytes both times, as the
bounty rules require.

## Licence

MIT — see `LICENSE`.
