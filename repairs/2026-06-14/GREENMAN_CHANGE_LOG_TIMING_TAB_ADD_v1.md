# GREENMAN CHANGE LOG - TIMING TAB ADD v1

Base file:
`Spell_app_v1_correct_styling_EMPTY_BOWL_REPAIR_v1_ANDROID_VIEW_FIX2.html`

Output file:
`Spell_app_v1_WORKING_SPELL_LIST_WITH_TIMING_TAB_v1.html`

## User instruction
Add the Moon / Planet / Hours timing page into the latest branch where the spell list works but Candle routing is still stuck. Do not go backwards and do not touch Spell Builder.

## Scope
Changed only:
- `PAGES.moon`

Not changed:
- `PAGES.spellHome`
- `PAGES.spellList`
- `PAGES.candle`
- Spell Builder routing
- Tracker
- Summary
- Print Pack
- Journal / BoS / Grimoire
- bottom tab list

## Data used
- Timing page source: `page.html`
- Timing item data: transformed from `ALL_ITEMS_from_selection.js`
- Source item count injected: 322

## Timing logic now present in Moon tab
- Internal nav buttons: Now / Hours / Moon
- Uses device clock through JavaScript `new Date()`
- Uses fixed Glastonbury Tor coordinates already in `page.html`:
  - LAT = 51.1444
  - LON = -2.7168
- Uses Chaldean order:
  Saturn → Jupiter → Mars → Sun → Venus → Mercury → Moon
- Calculates sunrise/sunset with the existing `sunTime()` function in the timing page.
- Calculates planetary hours with the existing `planetaryHoursForDate()` function.
- Calculates moon phase with the existing `moonPhase()` function.

## Direct code changes
1. Replaced embedded `PAGES.moon` with the uploaded `page.html` timing page.
2. Removed Google Fonts `@import` from that page so the app does not call the internet.
3. Removed the review note box from `page.html`.
4. Injected `window.GREENMAN_ITEM_DATABASE` from `ALL_ITEMS_from_selection.js`.
5. Set `localStorage.greenman_item_database` from that injected item database for the timing page to read.
6. Escaped embedded `</script>` tags as `<\/script>` so the outer app shell does not break.

## Validation
- Existing `PAGES` parsed before edit.
- New `PAGES` parsed after edit.
- Only Moon page was intentionally replaced.
- No Spell Builder pages were modified in this pass.
