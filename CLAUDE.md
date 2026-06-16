# Greenman HedgeWitchery App — working notes

This repo holds the spellbuilder app as single-file HTML builds
(`Spell_app_V6g.html`, `Spell_app_V7a.html`, etc). Each file is a shell
(~378 lines) plus one giant line containing `const PAGES = {...}` — a
JSON object holding all 15 pages (`home, admin, spellHome, spellList,
candle, selection, extraHerbs, journal, bos, grimoire, planets,
planetTiming, moon, numerology, printPack`) as JSON-escaped HTML/JS
strings. The shell loads each page into `#pageFrame` via
`d.open(); d.write(html); d.close();`.

## Critical rule when editing the PAGES line via Python json

If you do `obj = json.loads(...)` then `json.dumps(obj)` on the PAGES
object, you MUST re-escape `</script>` back to `<\/script>` before
writing the file back out:

```python
new_json = json.dumps(obj)
new_json = new_json.replace('</script>', '<\\/script>')
```

`json.dumps()` does not escape forward slashes by default. The pages
embed real `</script>` closing tags inside their own `<script>` blocks
(once decoded), which must stay escaped as `<\/script>` at the
outer-file level — otherwise the browser's HTML parser closes the
*outer* `<script>` tag containing `const PAGES = {...}` at the first
occurrence, corrupting/truncating everything after it. Symptom: most
of the app renders blank (only fragments before the first occurrence
show), even though `json.loads()` on the extracted PAGES object still
succeeds. This exact bug was fixed once before in commit `c418f10`
("Fix 42 unescaped `</script>` tags...") and was accidentally
reintroduced via a `json.dumps()` round-trip in this session — check
for it after any such edit.

## Verification checklist after every edit to the PAGES line

```python
import json
with open('Spell_app_V7a.html') as f:
    lines = f.readlines()
line = lines[98]  # giant PAGES line
start = line.index('const PAGES = ') + len('const PAGES = ')
end = line.rindex('};') + 1
obj = json.loads(line[start:end])  # must not raise
assert len(obj) == 15

# raw-text check: no unescaped </script> in the PAGES line itself
idx = 0
while True:
    i = line.find('</script>', idx)
    if i == -1: break
    assert line[i-1] == '\\', f'unescaped </script> at {i}'
    idx = i + 1
```

Also worth checking after edits: `<script` open-tag count outside the
PAGES line should equal `</script>` close-tag count outside the PAGES
line (these are the shell's own real script tags, 3 as of this
writing).

## Branch history

- `Spell_app_V6g.html` lives on `claude/sweet-archimedes-crcj64` —
  left untouched as a fallback.
- `Spell_app_V7a.html` lives on `claude/version-7a` — current cleanup
  work happens here. Branching does not "move" other files; every
  branch carries the full repo tree by definition.
