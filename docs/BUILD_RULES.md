# Greenman Build Rules

This repo is the clean rebuild home for Version 2.

## Golden rule

The working spell-builder must not be destroyed while cleaning other tabs.

Use the last known working query-first spell-builder as the baseline. Clean and reconnect one page at a time.

## Query-first rule

Pages must be empty bowls.

A page may contain:

- layout
- buttons
- placeholders
- render targets
- calls to the engine

A page must not contain:

- preselected Love spell
- preselected Pink candle
- preselected herbs/crystals/runes/oils/deities
- hardcoded summary values
- locked test Journal or BoS cards

Real item names are allowed only inside data files or live rendered output.

## One state rule

Everything must read from one spell state:

```js
spellState = {
  category: null,
  spell: null,
  spellKeywords: [],
  candle: null,
  selections: {
    earth: null,
    air: null,
    fire: null,
    water: null,
    crystal: null,
    rune: null,
    goddess: null,
    god: null,
    oil: null
  },
  matchedUses: {},
  associationReasons: {},
  currentStep: 'category',
  method: null,
  wordingTone: null
}
```

Tracker, Summary, Altar, Journal, BoS and Print Pack must all read from this same state.

## Reset rule

When category changes, clear spell, candle and all selections.

When spell changes, clear candle and all selections.

When candle changes, clear all selections from Earth onward.

When an earlier selection changes, clear later selections only.

This prevents old localStorage/test data from jumping the user to Oil.

## Testing rule

After every change, test this route on the phone:

```text
Home → Spell Builder → Category → Spell → Candle → Earth
```

Then test:

```text
Earth → Air → Fire → Water → Crystal → Rune → Goddess → God → Oil → Print Pack
```

Only after that, touch Journal, BoS, Grimoire, Timing, Moon or Numerology.