# Spell Builder Flow Map

This is the approved live flow for the query-first spell builder.

```text
Home
→ Spell Builder Home
→ Select Category
→ Select Spell
→ Choose Candle
→ Choose Earth Herb
→ Choose Air Herb
→ Choose Fire Herb
→ Choose Water Herb
→ Choose Crystal
→ Choose Rune
→ Choose Goddess
→ Choose God
→ Choose Oil
→ Summary / Altar
→ Wording Engine
→ Print Pack
```

## Step contracts

### Category

Source: `spells.json` or embedded spell category data.

Action: save `spellState.category` and clear all later state.

### Spell

Source: chosen category.

Action: save spell name, spell category and spell keywords. Tracker should show spell name.

### Candle

Source: candle data.

Ranking:

- spell keyword match
- candle magical uses
- category match

Display:

- top 3 first
- show more can reveal more

### Earth / Air / Fire / Water Herbs

Source: item data filtered by category Herb.

Filtering:

- match element exactly
- match chosen spell keywords/magical uses

Display card:

- item name
- ye olde name
- Latin
- element
- magical uses relevant to the selected spell only

Info sheet:

- full item record
- full magical uses
- powers
- Greenman Energy
- associations

### Crystal

Source: item data filtered by Crystal.

Ranking:

- spell keyword match
- associations to chosen herbs

Show 7 first, show more by 7.

### Rune

Source: item data filtered by Rune.

Ranking:

- spell keyword match
- associations to chosen herbs
- association to chosen crystal

Show 3 first, show more by 3.

### Goddess

Source: item data filtered by Deity.

Filtering:

- feminine/goddess and dual deities

Ranking:

- spell keyword match
- associated herbs
- associated crystal
- associated rune

### God

Source: item data filtered by Deity.

Filtering:

- masculine/god and dual deities
- if using a two-dual route, show dual choices correctly

Ranking:

- spell keyword match
- associated herbs
- associated crystal
- associated rune
- association with goddess selection where present

### Oil

Source: item data filtered by Oil.

Ranking:

- spell keyword match
- associated herbs
- associated crystal
- associated rune
- associated deities

### Summary / Altar / Print Pack

Must read only from `spellState`.

No locked Love, Pink, Rose Quartz, or sample item values may appear unless the user actually selected them.