# V1 preserved, V3 Timing tab transplanted

Date: 2026-06-14

## User correction

The original V1 file has the valuable working Book of Shadows. The previous repaired versions broke the BoS internals. The correct approach is to use the original V1 file as the base and transplant only the good planet/timing tab behaviour from Spell_app_V3.

## Source files used

- Base: `Spell_app_v1_correct_styling(1).html`
- Timing reference: `Spell_app_V3(2).html`
- Hours page: `HOURS PAGE working .html`

## What was changed

- Preserved the original V1 `PAGES.bos` string exactly.
- Preserved original V1 Journal and Book of Shadows internals.
- Changed bottom tab layout from 8 tabs to 7 tabs.
- Combined old separate `Planets` and `Moon` bottom tabs into one `Timing` bottom tab.
- Replaced only these timing page entries:
  - `PAGES.planets` from V3
  - `PAGES.moon` from V3
  - `PAGES.planetTiming` from the supplied Hours page, with a shell navigation bridge only
- Rewired the internal Now / Hours / Moon buttons so they call the shell route map instead of old standalone HTML filenames.
- Kept the Hours page visual/function body as supplied.
- Ran JavaScript syntax check on the rebuilt outer shell script.

## Output files

- `Spell_app_V1_with_V3_Timing_Tab_BoS_Preserved.html`
- `Spell_app_V1_with_V3_Timing_Tab_BoS_Preserved.zip`

## Safety note

This is not a full rebuild. It is a narrow timing-tab transplant into the original V1 base, with BoS preserved.