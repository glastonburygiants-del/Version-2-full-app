# Current Known Bugs and Causes

## 1. Blank brown screen

Common causes already seen:

- raw `</script>` inside embedded page strings closing the shell script early
- duplicate declarations such as `arrify` declared twice
- embedded page script crash before render

## 2. Choose Your Herb page empty

Cause found in query-first build:

- selection page JavaScript crashed before rendering cards
- duplicate `arrify` declaration was one cause

Fix principle:

- test each embedded page script separately
- render a visible error panel if card rendering fails

## 3. Jumping from Candle to Oil

Cause:

- old selections remain in localStorage
- resume logic thinks Earth/Air/Fire/Water/Crystal/Rune/Goddess are already chosen

Fix:

- clear downstream state when category/spell/candle changes
- never resume to a later step unless current state belongs to the current spell/category/candle

## 4. Tracker missing or wrong

Cause:

- tracker not wired to the single current spell state
- old hardcoded values such as `tier:'weaving'` and `spellHerbs:[]`

Fix:

- tracker reads `spellState` only
- tracker never owns or invents data

## 5. Summary / Print Pack locked on Love

Cause:

- old visual/test summary values left inside page code
- summary builder not using current spell state for every field

Fix:

- Summary reads only from spellState
- no field has a default Love/Pink/Rose value except blank placeholder text

## 6. Journal and BoS empty or wrong

Cause:

- pages simplified too far in the all-pages-clean attempt
- save/read model not yet connected cleanly to spellState and saved BoS entries

Fix:

- restore working shell
- rebuild Journal first as current spell list
- rebuild BoS second as saved entries from localStorage

## 7. Grimoire info cards too simple

Cause:

- simplified clean page dropped original rich Grimoire layout

Fix:

- keep query-first item data
- rebuild info sheet layout from original visual style

## 8. Moon / Timing / Numerology showing strings or rough values

Cause:

- old/debug text and simplified pages mixed together

Fix:

- one page at a time
- device clock functions live in one timing engine
- pages display only formatted results, never raw code values