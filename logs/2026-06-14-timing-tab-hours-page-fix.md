# Timing tab + Hours page fix

Date: 2026-06-14

## What changed

- Combined the separate bottom `Planets` and `Moon` tabs into one bottom tab: `Moon & Planets`.
- Added the uploaded `HOURS PAGE working .html` as a real shell page route: `PAGES.hours`.
- Removed the duplicate `PAGES.moon` route from the shell page map.
- Rewired the internal timing navigation so:
  - `Now` opens the existing `PAGES.planets` page.
  - `Hours` opens the new `PAGES.hours` page.
  - The old Moon button no longer jumps to a removed standalone Moon filename.
- Kept the Hours page using live device time via `new Date()` and the existing minute refresh.
- Confirmed the Hours page uses Glastonbury Tor as the sunrise/sunset calculation point: latitude `51.1444`, longitude `-2.7168`.
- Updated the shell bottom tab grid from 8 to 7 columns to match the new tab count.
- Added an in-file HTML change log comment to the generated fixed HTML.

## Files produced locally

- `Spell_app_v1_correct_styling_TIMING_TAB_FIXED.html`
- `Spell_app_v1_correct_styling_TIMING_TAB_FIXED.zip`

## Notes

This was done as a clean route/map change, not an overlay stack. The supplied Hours page was inserted as the Hours route and only its old standalone navigation jumps were rewired for the shell.