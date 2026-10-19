# Social Music: concept notes

Last updated: 20/10/2026. Personal working notes, not a legal filing. Brazil is first-to-file for patents, so this file establishes no patent priority.

## Purpose
A small wearable display that shows the album art of what you are listening to, as self-expression: the same pride as wearing an obscure band tee. Strangers reacting is a possible side effect, not the goal. The value is unilateral: the wearer gets it whether or not anyone recognizes the cover, so no network effect, density, or stranger interaction is needed.

## Founder decisions (stated by the founder, 19-20/10/2026)
- It is a display, not an interactive Spotify app. Minimalist, Apple-like: **one grip, one button, one light**.
- No touchscreen (extra cost and failure modes, little functionality).
- Screen leaning: tall 240x280 (about 1.69") so square album art sits on top with a strip below for song / album / artist. Leaning, not final.
- Modes switched by a physical button: **Now playing**, **Favorite**, and a possible third (TBD).
- A small light that is on only in Now-playing mode, so people around you can tell "playing now" from "my favorite".
- Back mechanism: a multi-grip clip that works on a shirt and on a bag (details to be developed).
- iPhone and Android both.
- Founder does not want to learn to code, but wants to understand what is going on. Claude writes code and explains it.
- Not buying hardware yet. No board chosen.

## Open questions (founder's call)
1. Third mode: what is it (last played, a second favorite, off)?
2. How many favorites, and how are they chosen? Needs a phone app at least for setup.
3. What shows in Now-playing mode when nothing is playing?
4. Display size: dev-board screens of this class are only about 28 mm wide (derived from the diagonal, verify on datasheet), not the 5 cm originally imagined.
5. Where it is worn, and the grip mechanism.
6. Third-party art source for a commercial product.

## Known weak points
1. Live feed is unfiltered: the Favorite mode and an off option are the answer; keep them.
2. "Mainstream people don't care" is doubtful: fandoms (idol, Swiftie, anime) are very expressive buyers. Test fandom as a segment.
3. Niche-taste buyers may prefer analog objects. Screen vs. aesthetic untested for wearables.
4. Minimalism conflicts with needing an app: art lookup needs internet, so the phone app has to exist even if it is nearly invisible. iPhone and Android need two different pipelines, so roughly double the testing.
5. A 40 px text strip on a ~28 mm-wide screen is about 5 mm tall: readable only at arm's length.

## Getting the content (provisional, Claude recommendation, not yet validated)
- Text (title, artist, album): system-level now-playing, source-agnostic, no streaming-service API.
  - iPhone: Apple Media Service (AMS) over Bluetooth LE. Public spec, working ESP32 examples (Adafruit, Moddable, ctrl01, MusicStation). Known iPhone reconnect/bonding quirks with ESP32 (forum reports).
  - Android: notification listener plus media session metadata.
- Album art: AMS carries no image, so look it up by artist and album (prototype: iTunes Search API, fallback MusicBrainz Cover Art Archive). Coverage for obscure music is untested.
- Open business risks: art-source terms for a commercial product; whether AMS needs Apple approval at commercial scale (unconfirmed).

## Buyer (working hypothesis)
Young adults (~18-30) for whom taste is part of identity, who already wear it (band tees, pins, patches, vinyl) and feel their real listening is invisible. Fandom is the test segment.

## Prototype plan (until early January 2027, while in France)
Options A-D were laid out (buy nothing / one board / several screens / wait for Brazil); no decision yet.
Free steps meanwhile: album-art coverage test, enclosure model with placeholder dimensions, firmware skeleton.

## Later (Brazil, from January)
Sebraetec, SENAI Laboratorio Aberto (BH), MEI registration; investors only after a working prototype and real unit economics.

## Update 21/10/2026: sizes, power, markets
- Two sizes under consideration (founder): a small ~3 cm pin (dev-board class screens are about 28 mm wide), and a main ~5 cm product that also shows the song name. Not decided.
- A 2.8" portrait 480x640 panel is about 43 x 57 mm: a ~43 mm square cover plus a ~14 mm text strip. Closest found to the ~5 cm idea (verify the exact module before buying). The 2.8" 480x480 Waveshare board is round (about 71 mm across), too big.
- Battery (open): rough arithmetic (not measured) gives about 2-4 h on a 400 mAh cell with an unoptimized dev board. A shipping product of this class (Divoom Emodo, 1.8") claims 8 h+. All-day wear needs optimization and/or a bigger battery, which means a thicker badge.
- Charging (open): USB-C (simple, adds a port), magnetic contacts (minimalist, needs custom cable/dock), wireless (coil adds thickness and cost).
- Markets (open): US is ~58-60% iPhone (web traffic), Brazil ~75-81% Android. Founder sees the US as a better-paying main market. Implication: iPhone first for the US, Android first for Brazil. Radio-emitting products need per-market certification (unverified specifics).

## Update 22/10/2026: art coverage test and e-ink vs LCD
- Album-art coverage (18 albums, mainstream to underground, run 22/10): iTunes 16/18, Deezer 16/18, Cover Art Archive 17/18, at least one source found 17/18. The miss was Matuê "30PRAUM" (possibly a title/spelling issue). "Found" means a result was returned, not that the right edition was verified. iTunes returned HTTP 403 when queried quickly (rate limit), so retries are needed.
- Color e-ink: Spectra 6 (6 colors) full refresh about 19 s with flashing and no partial refresh (4" Waveshare panel, manufacturer figure; a retailer says 10 s). No small Kaleido 3 modules found (7.8" and up only). A 4" Spectra 6 panel is about 85 x 56 mm.
- Panel-only price: 4" Spectra 6 about $38-47 (panel only, needs a driver board), vs. a whole 1.69" ESP32 LCD board at $16-22.
- Simulation (approximate, Claude-built): Spectra 6 dithers photographic covers heavily and mutes colors; graphic/text covers survive. Not a photo of a real panel.
- Charging: USB-C cheapest and easiest; Qi the most complex and costly; magnetic pogo in between but needs custom tooling. Component-level prices are weak supplier claims.
- Open: LCD for the prototype and e-ink later, or buy a small e-ink panel early to test the refresh feel.
