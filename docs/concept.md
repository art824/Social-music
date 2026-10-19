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
