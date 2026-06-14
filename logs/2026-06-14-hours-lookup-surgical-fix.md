# Hours lookup surgical fix

Date: 2026-06-14

## Request

Redo the Hours lookup as a surgical code replacement only. Do not replace the page, do not disturb the header/layout, and use the stable build from before the layout drift.

## Fix applied

Base file:
- `Spell_app_V1_with_V3_Timing_Tab_BoS_Preserved_HOURS_KEYBOARD_PROMPTS_FIXED.html`

Changed only inside the Hours page JavaScript:
- Replaced `loadDatabase()`.
- Replaced `findItems(q)`.

## Behaviour

- Hours now uses the full embedded item database extracted from the existing V1 Grimoire data.
- Search order is:
  1. Name exact/start/contains
  2. Ye Olde Name exact/start/contains
- Deity entries search by Name only.
- Amethyst is included in the Hours search database.
- Existing V1 BoS and layout/header were not replaced.

## Output files

- `Spell_app_V1_with_V3_Timing_Tab_BoS_Preserved_HOURS_LOOKUP_SURGICAL_FIXED.html`
- `Spell_app_V1_with_V3_Timing_Tab_BoS_Preserved_HOURS_LOOKUP_SURGICAL_FIXED.zip`
