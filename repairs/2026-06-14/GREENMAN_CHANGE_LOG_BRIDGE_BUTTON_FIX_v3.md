# GREENMAN CHANGE LOG - BRIDGE BUTTON FIX v3

Base file: `Spell_app_v1_correct_styling_EMPTY_BOWL_REPAIR_v1_ANDROID_VIEW_FIX2.html`
Output file: `Spell_app_v1_correct_styling_EMPTY_BOWL_REPAIR_v3_BRIDGE_BUTTON_FIX.html`

## Issue
Spell List now displays the correct spells, but tapping a spell does not move to the Candle page.

## What changed
Embedded page changed: `PAGES.spellList` only.

No changes to:
- `selectSpell()` direct parent messaging
- `candle`
- `spellHome`
- Over 18 category page
- Tracker
- Moon / Planets / Hours
- Journal / BoS / Grimoire
- Print Pack

## Proper button logic used
The page button remains page-local:

```text
button tap
↓
selectSpell() saves state and shows selected note
↓
existing shell bridge sees the spell button click
↓
shell bridge sends spellSelected
↓
shell bridge sends nav to candle
```

This avoids the bad v2 bandage:

```text
selectSpell() directly parent.postMessage(...)
```

## Exact code changed 1
In `renderSpellList()`, spell buttons now include data attributes so the existing shell bridge can read the spell and moon phase cleanly.

Before:

```js
return '<button class="spell-btn" onclick="selectSpell(' + JSON.stringify(name) + ',' + JSON.stringify(phase) + ')">' +
```

After:

```js
return '<button class="spell-btn" data-gm-spell=' + JSON.stringify(name) + ' data-gm-phase=' + JSON.stringify(phase) + ' onclick="selectSpell(' + JSON.stringify(name) + ',' + JSON.stringify(phase) + ')">' +
```

## Exact code changed 2
Replaced the old `window.selectSpell = function(...) { ... send nav ... }` wrapper in the page bridge with a delegated button click listener.

Reason:
- Do not overwrite `selectSpell()`.
- Let the local page function stay local.
- Keep parent navigation in the shell bridge only.
- Avoid duplicate/double route paths.

## Validation
- `PAGES` JSON parsed successfully after the edit.
- Only `PAGES.spellList` was changed from the one-step good file.
