# Timing tab repair after review

Date: 2026-06-14

## Problem reported

- The previous timing fix removed or hid the BoS page.
- The real Moon page was lost.
- The Hours page was not reachable.
- The Now page still showed the frozen test date `3 June 2026`.

## Repair applied

- Restored the bottom `BoS` tab entry.
- Kept the real `PAGES.moon` route instead of removing Moon entirely.
- Added a separate `PAGES.hours` route using the uploaded `HOURS PAGE working .html`.
- Removed the old duplicate `PAGES.planetTiming` route from the shell page map.
- Kept one bottom tab labelled `Moon & Planets`.
- Rewired the internal timing page buttons:
  - `Now` -> `PAGES.planets`
  - `Hours` -> `PAGES.hours`
  - `Moon` -> `PAGES.moon`
- Rebuilt the Now page date section from the device clock, removing the hardcoded `3 June 2026` value.
- Preserved the Hours page Glastonbury Tor constants from the supplied file: latitude `51.1444`, longitude `-2.7168`.
- Ran `node --check` against the rebuilt outer shell script after escaping embedded page scripts.

## Local output files

- `Spell_app_v1_correct_styling_TIMING_TAB_REPAIRED.html`
- `Spell_app_v1_correct_styling_TIMING_TAB_REPAIRED.zip`
