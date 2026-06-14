# GREENMAN CHANGE LOG - EMPTY BOWL REPAIR v1

Base file: `Spell_app_v1_correct_styling.html`
Local repaired artifact: `Spell_app_v1_correct_styling_EMPTY_BOWL_REPAIR_v1.html`
Date: 2026-06-14

## Repair rule
Changed the existing page code directly inside the working shell. I did not add a second shell, second tracker, second tab bar, iframe overlay, or duplicate routing layer.

## Scope changed
Only these embedded pages were changed:

1. `spellList`
2. `candle`

Not changed in this pass:

- Moon tab
- Planets tab
- Hours page
- Selection pages
- Tracker
- Journal
- BoS
- Grimoire
- Print Pack

---

# 1. spellList changes

## Changed code location
Embedded page: `PAGES.spellList`

Generated page-line changes from the extracted embedded page:

- Original page lines 338-340 changed to repaired page lines 338-340.
- Original page lines 352-393 changed to repaired page line 352.
- New dynamic script inserted at repaired page lines 376-608.

## Original code removed, page lines 338-340

```html
<span class="cat-icon">&#10084;</span>
<div class="cat-title">Attraction, Love &amp; Relationships</div>
<div class="cat-count">8 spells</div>
```

## New code used, page lines 338-340

```html
<span class="cat-icon" id="catIcon">&#10022;</span>
<div class="cat-title" id="catTitle">Choose Spell</div>
<div class="cat-count" id="catCount">0 spells</div>
```

## Original code removed, page lines 352-393

This was the hardcoded Love-category spell list:

```html
<section class="spell-list" aria-label="Spell list">
  <button class="spell-btn" onclick="selectSpell('Love','Waxing')">Love</button>
  <button class="spell-btn" onclick="selectSpell('Attraction','Waxing')">Attraction</button>
  <button class="spell-btn" onclick="selectSpell('Exploring feelings','Waxing')">Exploring feelings</button>
  <button class="spell-btn" onclick="selectSpell('Fidelity','Waxing')">Fidelity</button>
  <button class="spell-btn" onclick="selectSpell('Weddings / Handfastings','Full')">Weddings / Handfastings</button>
  <button class="spell-btn" onclick="selectSpell('Soul Mate drawing','Waxing')">Soul Mate drawing</button>
  <button class="spell-btn" onclick="selectSpell('Friendship','Waxing')">Friendship</button>
  <button class="spell-btn" onclick="selectSpell('Passion','Waxing')">Passion</button>
</section>
```

## New code used, page line 352

```html
<section class="spell-list" id="spellListHost" aria-label="Spell list"></section>
```

## New spellList script behaviour, page lines 376-608

The new script:

- Reads `gm_new_shell_spell_state_v1.category`.
- Renders only the spell list for that chosen category.
- Saves the chosen spell back to `gm_new_shell_spell_state_v1.spell`.
- Clears candle and later ingredient selections when a new spell is chosen.
- Keeps the existing shell bridge route to Candle.

Core code used:

```js
function getShellSpellState() {
  try { return JSON.parse(localStorage.getItem('gm_new_shell_spell_state_v1') || '{}') || {}; }
  catch(e) { return {}; }
}

function saveShellSpellState(next) {
  try { localStorage.setItem('gm_new_shell_spell_state_v1', JSON.stringify(next || {})); }
  catch(e) {}
}

function getSelectedCategory() {
  var state = getShellSpellState();
  return state.category || 'Attraction, Love & Relationships';
}

function renderSpellList() {
  var category = getSelectedCategory();
  var spells = SPELLS_BY_CATEGORY[category] || [];
  var host = document.getElementById('spellListHost');
  var title = document.getElementById('catTitle');
  var count = document.getElementById('catCount');
  var icon = document.getElementById('catIcon');

  if (title) title.textContent = category;
  if (count) count.textContent = spells.length + (spells.length === 1 ? ' spell' : ' spells');
  if (icon) icon.innerHTML = SPELL_CATEGORY_ICONS[category] || '&#10022;';

  if (!host) return;

  host.innerHTML = spells.map(function(name) {
    var phase = moonForSpell(name);
    return '<button class="spell-btn" onclick="selectSpell(' + JSON.stringify(name) + ',' + JSON.stringify(phase) + ')">' +
      '<span class="spell-left-icon">' + (SPELL_CATEGORY_ICONS[category] || '&#10022;') + '</span>' +
      '<span class="spell-name">' + escapeHtml(name) + '</span>' +
      '<span class="moon-side"><span class="moon-icon">&#127762;</span><span class="moon-name">' + escapeHtml(phase) + '</span></span>' +
    '</button>';
  }).join('');
}

function selectSpell(name, phase) {
  var state = getShellSpellState();
  var category = state.category || getSelectedCategory();
  state.spell = { category: category, spell: name, name: name, moonPhase: phase };
  state.candle = null;
  state.selections = { earth:null, air:null, fire:null, water:null, crystal:null, rune:null, goddess:null, god:null, oil:null };
  saveShellSpellState(state);
}

document.addEventListener('DOMContentLoaded', renderSpellList);
```

---

# 2. candle changes

## Changed code location
Embedded page: `PAGES.candle`

Generated page-line changes from the extracted embedded page:

- Original page line 187 changed to repaired page line 187.
- Original static candle card block lines 189-252 replaced by repaired page line 189.
- Original candle data/script block lines 317 onward replaced by dynamic candle script.

## Original code removed, page line 187

```html
<div class="subtitle">Ranked by alignment to your Love spell</div>
```

## New code used, page line 187

```html
<div class="subtitle" id="candleSubtitle">Ranked by alignment to your selected spell</div>
```

## Original code removed, page lines 189-252

This was the hardcoded Love candle ranking:

```html
<!-- CANDLE CARDS — ranked by keyword match to Love spell -->
<!-- Pink — best match (love, romance) -->
<!-- Red — 2nd match (love, passion) -->
<!-- Orange — 3rd match (attraction) -->
```

## New code used, page line 189

```html
<section id="candleCardsHost" aria-label="Candle choices"></section>
```

## New candle script behaviour

The new script:

- Reads the selected spell from `gm_new_shell_spell_state_v1.spell`.
- Reads the selected category from `gm_new_shell_spell_state_v1.category`.
- Uses the embedded `EDITOR_DATA["Candles"]` rows already in this app file.
- Scores all 13 candle colours against the selected spell/category.
- Displays the top 3 ranked candle cards.
- Saves the chosen candle back to `gm_new_shell_spell_state_v1.candle`.
- Keeps the original tracker slot fill and altar popup behaviour.

Core code used:

```js
function getShellSpellState() {
  try { return JSON.parse(localStorage.getItem('gm_new_shell_spell_state_v1') || '{}') || {}; }
  catch(e) { return {}; }
}

function saveShellSpellState(next) {
  try { localStorage.setItem('gm_new_shell_spell_state_v1', JSON.stringify(next || {})); }
  catch(e) {}
}

function keywordsForSpell(state) {
  var spell = (state.spell && (state.spell.name || state.spell.spell)) || '';
  var category = (state.spell && state.spell.category) || state.category || '';
  var base = String(spell).toLowerCase().split(/[^a-z]+/).filter(function(w){ return w.length > 2; });
  return base.concat(CANDLE_CATEGORY_KEYWORDS[category] || []);
}

function candleScore(row, keywords) {
  var text = (row._name + ' ' + row['Magical Uses'] + ' ' + row['Spiritual Uses'] + ' ' + row['Deity / God']).toLowerCase();
  var score = 0;
  keywords.forEach(function(k) {
    k = String(k || '').toLowerCase();
    if (!k) return;
    if (text.indexOf(k) !== -1) score += k.indexOf(' ') !== -1 ? 4 : 2;
  });
  if (row._name === 'White') score += 1;
  return score;
}

function renderCandleChoices() {
  var state = getShellSpellState();
  var spellName = (state.spell && (state.spell.name || state.spell.spell)) || 'selected';
  var host = document.getElementById('candleCardsHost');
  var subtitle = document.getElementById('candleSubtitle');
  if (subtitle) subtitle.textContent = 'Ranked by alignment to your ' + spellName + ' spell';

  var keywords = keywordsForSpell(state);
  var ranked = CANDLE_ROWS.map(function(row, index) {
    return { row: row, index: index, score: candleScore(row, keywords) };
  }).sort(function(a,b) {
    return (b.score - a.score) || (a.index - b.index);
  }).slice(0,3);

  host.innerHTML = ranked.map(function(item, i) {
    var row = item.row;
    var colour = row._name;
    var element = CANDLE_ELEMENTS[colour] || 'Spirit';
    return '<div class="candle-card ' + (i===0 ? 'best' : '') + '">...</div>';
  }).join('');
}

function selectCandle(colour, element) {
  var state = getShellSpellState();
  state.candle = { colour: colour, color: colour, element: element };
  saveShellSpellState(state);
  // original tracker and altar fill code then runs
}

document.addEventListener('DOMContentLoaded', renderCandleChoices);
```

---

# Validation run

Checked locally after repair:

- `PAGES` JSON parsed successfully.
- `spellList` script syntax passed with `node --check`.
- `candle` script syntax passed with `node --check`.

# Important note

The app HTML is around 5 MB. The full repaired file is available as the ChatGPT artifact from this repair pass. The GitHub file named `Spell_app_v1_correct_styling_EMPTY_BOWL_REPAIR_v1.html` was marked `DO NOT USE` because it was only a placeholder path. This markdown log is the GitHub code ledger for the exact repair.