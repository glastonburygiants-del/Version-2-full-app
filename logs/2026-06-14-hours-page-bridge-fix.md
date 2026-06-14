# Hours page bridge fix

Date: 2026-06-14

## Problem reported

The V1-preserved / V3-timing build was close, but the Hours page did not render correctly from the combined Timing tab.

## Cause found

`PAGES.planetTiming` was using the supplied Hours page body, but it did not have the shell bridge that the V3 Timing pages use. Its original standalone `goMoonPlanetTab()` still pointed at old standalone HTML filenames, so once inside the shell the Hours page was not properly wired back into the shell route map.

## Fix applied

- Kept the previous V1-preserved build as the base.
- Kept V1 `PAGES.bos` preserved.
- Kept V3 `PAGES.planets` and `PAGES.moon` routes.
- Added a small Hours-only shell bridge to the supplied Hours page.
- Overrode the Hours page `goMoonPlanetTab()` so:
  - `Hours` stays on the Hours page and jumps to its search panel.
  - `Now` sends the parent shell to `PAGES.planets`.
  - `Moon` sends the parent shell to `PAGES.moon`.
- Left the Hours page visual/function body as supplied.
- Ran JavaScript syntax check on the rebuilt outer shell script.

## Output files

- `Spell_app_V1_with_V3_Timing_Tab_BoS_Preserved_HOURS_BRIDGE_FIXED.html`
- `Spell_app_V1_with_V3_Timing_Tab_BoS_Preserved_HOURS_BRIDGE_FIXED.zip`
