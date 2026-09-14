# Version Audit — V1 → V2 → V3

Audited: 2026-06-13

---

## Files

| File | Lines | Size | Purpose |
|------|-------|------|---------|
| `Spell_app_v1_correct_styling.html` | 168 | 4.9 MB | **V1 — Reference styling. All pages working. 8 tabs.** |
| `Spell_app_V2_engine_in.html` | 175 | 5.1 MB | **V2 — Engine added. State injected into pages. 7 tabs.** |
| `Spell_app_V3.html` | 17,219 | 5.1 MB | **V3 — Query-first empty bowls. Template literal format. Missing admin.** |

All three are single-file shell apps. Pages live inside a `PAGES` object in the shell script.

---

## Shell differences

| Feature | V1 | V2 | V3 |
|---------|----|----|-----|
| Tab count | **8** | 7 | 7 |
| Bottom tab grid | `repeat(8,1fr)` | `repeat(7,1fr)` | `repeat(7,1fr)` |
| Page format | JSON strings `"key": "..."` | JSON strings | Template literals `` key: `...` `` |
| Data injection | None — pages read localStorage | `window.__GM_SHELL_STATE__` injected into: selection, printPack, extraHerbs, deityHerbs | `window.__GM_STATE__` + `__GM_ITEMS__` + `__GM_KEYWORDS__` injected into: selection, candle, printPack, extraHerbs, deityHerbs, grimoire |
| State variable name | `appState` | `appState` | `appState` |

---

## Tabs

| Tab | V1 | V2 | V3 |
|-----|----|----|-----|
| Home ✦ | ✓ | ✓ | ✓ |
| Spell Builder 🕯 | ✓ | ✓ | ✓ |
| Journal 📜 | ✓ | ✓ | ✓ |
| BoS 📖 | ✓ | ✓ | ✓ |
| Grimoire 🌿 | ✓ | ✓ | ✓ |
| Planets ☉ | ✓ **separate tab** | — merged | — merged |
| Moon ☾ | ✓ **separate tab** | — | — |
| Timing ☾ | — | ✓ merged | ✓ merged |
| Numbers # | ✓ | ✓ | ✓ |

V1 has Planets and Moon as **separate tabs** (8 total). V2 merged them into one Timing tab (7 total). V3 keeps the 7-tab layout.

---

## Pages present in each version

| Page key | V1 | V2 | V3 | Notes |
|----------|----|----|-----|-------|
| home | ✓ | ✓ | ✓ | Same styling all three |
| admin | ✓ | ✓ | **✗ MISSING** | V3 dropped admin page entirely |
| spellHome | ✓ | ✓ | ✓ | |
| spellList | ✓ | ✓ | ✓ | |
| candle | ✓ | ✓ | ✓ | |
| selection | ✓ | ✓ | ✓ | V3 version is the new query-first tracker build |
| extraHerbs | ✓ | ✓ | ✓ | |
| deityHerbs | ✓ | ✓ | ✓ | |
| journal | ✓ | ✓ | ✓ | |
| bos | ✓ | ✓ | ✓ | |
| grimoire | ✓ | ✓ | ✓ | V1 and V3 use the same v25 rich grimoire page |
| planets | ✓ | ✓ | ✓ | |
| planetTiming | ✓ | ✓ | ✓ | |
| moon | ✓ | ✓ | ✓ | |
| numerology | ✓ | ✓ | ✓ | |
| summary | ✓ | **✗** | **✗** | V1 has summary page; V2/V3 use printPack instead |
| printPack | — | — | — | Referenced in routing logic but not in V3 PAGES |

---

## Grimoire page

V1 and V3 contain the **identical grimoire page** — "Greenman Grimoire Review v25 Popup Header Back Button".

It is a **full, rich, multi-section grimoire** with:
- Round filter buttons (type/category) 
- Element filter row (Earth / Air / Fire / Water)
- Keyword search input
- Small info cards — name, ye olde name, icon, magical uses, powers, Greenman energy, tags
- Full A4 popup detail view for each item
- Planet hours panel
- Reference tables (candles, elements, numerology)
- Spell match display

V2's grimoire page needs auditing separately — it was not confirmed identical.

The **new grimoire page** added in the latest `greenman_v1_QUERY_FIRST_RESTORE_LAST_WORKING_SPELLBUILDER_v4.html` rebuild is a simplified version. It should be **replaced with the V1/V3 rich grimoire page** (v25) if the full feature set is needed.

---

## Styling — what makes V1 "correct"

V1's home page and all inner pages use the same design tokens consistently:

### Fonts (correct — from V1)
```
font-family: 'Cinzel', serif          — headings, labels, uppercase
font-family: 'Crimson Text', serif    — body text, italic passages  
font-family: 'IM Fell English', serif — decorative large item names
```

### Shell background (V1/V2/V3 all match)
```css
--bg:    #3a2a18   (outer shell brown)
--green: #2d4a1e   (tab bar, header green)
--gold:  #c9a84c   (border gold)
--gold2: #e8c040   (bright gold active)
--cream: #f5ead0   (parchment)
--ink:   #1a0e04   (dark text)
```

### Page background (inner pages, all match)
```css
--bg: #2a1a08      (darker inner page)
```

---

## Data injection — incompatibility warning

V2 and V3 use **different variable names** for injected state:

| Version | Variable injected | Pages that expect it |
|---------|------------------|----------------------|
| V2 | `window.__GM_SHELL_STATE__` | selection, extraHerbs, deityHerbs |
| V3 | `window.__GM_STATE__` + `window.__GM_ITEMS__` | selection, extraHerbs, deityHerbs, candle, grimoire |

If a V2 shell loads a V3 inner page (or vice versa) the state will not arrive. Each page must read from the variable name its shell injects.

---

## What V3 has that V1/V2 don't

1. **Query-first selection page** — full ranking engine inline, tracker rendered in page, items from `__GM_ITEMS__`
2. **Template literal PAGES** — readable, one page per block, easy to edit
3. **Grimoire receives GM_ITEMS** — data injected so item list is live not hardcoded
4. **Candle gets state injection** — candle page can read spell keywords from shell state
5. **Cleaner message routing** — `itemSelected`, `categorySelected`, `spellSelected`, `candleSelected` all handled

## What V1 has that V3 is missing / broke

1. **Admin page** — completely absent from V3 PAGES
2. **Summary page** — V1 has `summary`; V3 has no summary or printPack in PAGES
3. **Separate Moon tab** — V1 has Planets and Moon as separate tabs giving richer navigation
4. **Working data flow** — V1 uses localStorage throughout so pages always find their data; V3 pages that depend on injection will fail if shell doesn't inject

---

## Recommended rebuild path

Use **V3 as the base** (query-first, template literals, best engine).

Port these specific things **from V1 into V3**:
1. Copy `admin` page from V1 into V3 PAGES
2. Copy `summary` page from V1 into V3 PAGES (or confirm printPack covers it)
3. Consider restoring Planets + Moon as two separate tabs if the combined Timing tab is losing features
4. Replace the simplified grimoire page in the current `greenman_v1_QUERY_FIRST_RESTORE_LAST_WORKING_SPELLBUILDER_v4.html` with the V1/V3 v25 rich grimoire page, then update it to read from `window.__GM_ITEMS__` (already injected by latest shell fix)
