# Social Music: concept notes

Last updated: 19/10/2026. Personal working notes, not a legal filing. Brazil is first-to-file for patents, so this file establishes no patent priority.

## Purpose
A small wearable display that shows the album art of what you are listening to, as self-expression: the same pride as wearing an obscure band tee. Strangers reacting is a possible side effect, not the goal. The value is unilateral: the wearer gets it whether or not anyone recognizes the cover, so no network effect, density, or stranger interaction is needed.

## Known weak points
1. A live feed is unfiltered. Needs modes: Live, Pinned (hold the album you're proud of), Off.
2. Assumption "mainstream people don't care" is doubtful. Fandoms (idol, Swiftie, anime) are very expressive buyers. Test fandom as a segment.
3. Niche-taste buyers may prefer analog objects. Screen vs. aesthetic is untested for wearables (Tuneshine sells at $199, but as a desk object).

## Getting the content (provisional, Claude recommendation, not yet validated)
- Text (title, artist, album): system-level now-playing, source-agnostic, no streaming-service API.
  - iPhone: Apple Media Service (AMS) over Bluetooth LE. Public spec, working ESP32 examples (Adafruit, Moddable, ctrl01, MusicStation).
  - Android: notification listener plus media session metadata.
- Album art: AMS carries no image, so look it up by artist and album (prototype: iTunes Search API, fallback MusicBrainz Cover Art Archive). Android can often take art from the player directly.
- Open business risks: art-source terms for a commercial product (iTunes terms are gray); whether AMS needs Apple approval at commercial scale (unconfirmed).

## Form factor (provisional, open for the founder to decide)
- Pin/clip badge for bag strap, jacket, collar or lanyard; headphone-band mount as an accessory. The Bluetooth link goes to the phone, so the badge does not depend on headphones.
- Square color LCD (~1.5", 240x240), album art only; caption toggle later. E-ink is a later question.

## Buyer (working hypothesis)
Young adults (~18-30) for whom taste is part of identity, who already wear it (band tees, pins, patches, vinyl) and feel their real listening is invisible. Fandom is the test segment.

## Prototype plan (until early January 2027, while in France)
1. Buy an ESP32 board with a color screen and battery connector (~EUR 20-40).
2. Firmware: AMS text on screen first, then art via phone hotspot (approach from MusicStation, MIT licensed).
3. Enclosure: parametric 3D model (STL), printed at a makerspace, fab lab or online service.
4. Test by wearing it. Wearer-side signals first (days worn, how often you want to hide a track); spontaneous reactions are a bonus.

## Later (Brazil, from January)
Sebraetec, SENAI Laboratorio Aberto (BH), MEI registration; investors only after a working prototype and real unit economics.
