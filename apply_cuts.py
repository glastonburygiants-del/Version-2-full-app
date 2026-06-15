#!/usr/bin/env python3
"""Apply cleanup cuts to Spell_app_V6a.html -> Spell_app_V6b.html"""

import os

src = '/home/user/Version-2-full-app/Spell_app_V6a.html'
dst = '/home/user/Version-2-full-app/Spell_app_V6b.html'

print(f"Reading {src} ...")
content = open(src, encoding='utf-8').read()
original_len = len(content)
print(f"  Original size: {original_len:,} chars\n")

# ── STEP 1: Remove the two HTML comment blocks at the very top (before <html lang="en">) ──
step1_blocks = [
    '<!--\nGREENMAN BRIDGE CLEANUP COPY — generated from uploaded file; page CSS/markup preserved, repeated generic bridge blocks trimmed per page.\n-->',
    '<!--\nGREENMAN TIMING TAB PATCH — 2026-06-14\nSource base: original V1 file supplied by user.\nPreserved: original V1 Journal and Book of Shadows page strings unchanged.\nChanged only:\n- bottom tabs: Planets + Moon combined into one Timing tab\n- PAGES.planets and PAGES.moon copied from supplied Spell_app_V3.html timing implementation\n- PAGES.planetTiming replaced with supplied HOURS PAGE working .html, with only shell navigation bridge added\n- internal Now / Hours / Moon buttons route through the shell instead of dead standalone filenames\n-->',
]
print("STEP 1: Remove top-of-file HTML comment blocks")
for i, block in enumerate(step1_blocks, 1):
    if block in content:
        before = len(content)
        content = content.replace(block, '', 1)
        print(f"  Block {i}: removed {before - len(content):,} chars")
    else:
        print(f"  Block {i}: NOT FOUND — check text!")

# ── STEP 2: Remove inline changelog HTML comment blocks inside <head> ──
step2_blocks = [
    '<!-- 2026-06-14: Hours page bridge fixed; V1 BoS still preserved; V3 timing routes retained. -->',
    '<!--\nCHANGE LOG 2026-06-14 — Hours keyboard prompt match\n- Kept V1 base and existing BoS intact.\n- Kept V3 Timing/Moon wiring intact.\n- Changed Hours page keyboard/search prompt to match Moon page wording.\n- Keyboard display now shows the prompt when empty instead of a blank line.\n-->',
]
print("\nSTEP 2: Remove inline changelog comment blocks inside <head>")
for i, block in enumerate(step2_blocks, 1):
    if block in content:
        before = len(content)
        content = content.replace(block, '', 1)
        print(f"  Block {i}: removed {before - len(content):,} chars")
    else:
        print(f"  Block {i}: NOT FOUND — check text!")

# ── STEP 3: Remove <div id="gmDebugNums" ...>...</div> ──
print("\nSTEP 3: Remove <div id=\"gmDebugNums\"> element")
debug_div = '<div id="gmDebugNums" style="position:fixed;bottom:70px;left:4px;background:rgba(0,0,0,.6);color:#0f0;font-size:8px;padding:3px;font-family:monospace;z-index:99999;text-align:left;pointer-events:none;line-height:1.3;">debug...</div>'
if debug_div in content:
    before = len(content)
    content = content.replace(debug_div, '', 1)
    print(f"  Removed {before - len(content):,} chars")
else:
    print("  NOT FOUND — check text!")

# ── STEP 4: Remove the try/catch debug block inside setAppHeight() ──
print("\nSTEP 4: Remove try/catch debug block inside setAppHeight()")
try_block = (
    "  try{\n"
    "    var sh = document.getElementById('gmShell');\n"
    "    var r = sh ? sh.getBoundingClientRect() : null;\n"
    "    var dn = document.getElementById('gmDebugNums');\n"
    "    if(dn){\n"
    "      dn.innerHTML =\n"
    "        'innerW/H: '+window.innerWidth+' x '+window.innerHeight+'<br>'+\n"
    "        'visualViewport: '+(vv?Math.round(vv.width)+' x '+Math.round(vv.height):'n/a')+'<br>'+\n"
    "        'docEl client: '+document.documentElement.clientWidth+' x '+document.documentElement.clientHeight+'<br>'+\n"
    "        '--app-h: '+h+'px<br>'+\n"
    "        '#gmShell rect: '+(r?Math.round(r.width)+' x '+Math.round(r.height)+' @ ('+Math.round(r.left)+','+Math.round(r.top)+')':'not found');\n"
    "    }\n"
    "  }catch(e){\n"
    "    var dn2 = document.getElementById('gmDebugNums');\n"
    "    if(dn2) dn2.textContent = 'setAppHeight error: '+e.message;\n"
    "  }\n"
)
if try_block in content:
    before = len(content)
    content = content.replace(try_block, '', 1)
    print(f"  Removed {before - len(content):,} chars")
else:
    print("  NOT FOUND — check text!")

# ── STEP 5: Remove function pageTitle(page){...} entirely ──
print("\nSTEP 5: Remove function pageTitle(page){...}")
page_title_fn = "function pageTitle(page){return (PAGES[page]||'').slice(0,80)}\n"
if page_title_fn in content:
    before = len(content)
    content = content.replace(page_title_fn, '', 1)
    print(f"  Removed {before - len(content):,} chars")
else:
    print("  NOT FOUND — check text!")

# ── STEP 6: Update tabFor() to remove 'deityHerbs' and 'summary' ──
print("\nSTEP 6: Update tabFor() condition")
old_tabfor = "if(['spellHome','spellList','candle','selection','extraHerbs','deityHerbs','summary','printPack'].includes(page)) return 'spellHome';"
new_tabfor = "if(['spellHome','spellList','candle','selection','extraHerbs','printPack'].includes(page)) return 'spellHome';"
if old_tabfor in content:
    before = len(content)
    content = content.replace(old_tabfor, new_tabfor, 1)
    print(f"  Replaced; size change: {before - len(content):,} chars removed")
else:
    print("  NOT FOUND — check text!")

# ── STEP 7: Remove `page==='summary' ||` from showPage localStorage condition ──
print("\nSTEP 7: Remove page==='summary' || from showPage")
old_summary_check = "  if(page==='summary' || page==='printPack') saveSummaryToLocalStorage();\n"
new_summary_check = "  if(page==='printPack') saveSummaryToLocalStorage();\n"
if old_summary_check in content:
    before = len(content)
    content = content.replace(old_summary_check, new_summary_check, 1)
    print(f"  Replaced; size change: {before - len(content):,} chars removed")
else:
    print("  NOT FOUND — check text!")

# ── STEP 8: Remove PAGES.summary (from ,"summary":" to ,"printPack":") ──
print("\nSTEP 8: Remove PAGES.summary entry")
s_start = content.find(',"summary":"')
s_end = content.find(',"printPack":"')
if s_start != -1 and s_end != -1:
    removed_block = content[s_start:s_end]
    before = len(content)
    content = content[:s_start] + content[s_end:]
    print(f"  Removed {before - len(content):,} chars (summary page block)")
else:
    print(f"  NOT FOUND — summary at {s_start}, printPack at {s_end}")

# ── STEP 9: Remove PAGES.deityHerbs (from ,"deityHerbs":" to ,"journal":") ──
print("\nSTEP 9: Remove PAGES.deityHerbs entry")
d_start = content.find(',"deityHerbs":"')
d_end = content.find(',"journal":"')
if d_start != -1 and d_end != -1:
    before = len(content)
    content = content[:d_start] + content[d_end:]
    print(f"  Removed {before - len(content):,} chars (deityHerbs page block)")
else:
    print(f"  NOT FOUND — deityHerbs at {d_start}, journal at {d_end}")

# ── Write output ──
print(f"\nWriting {dst} ...")
open(dst, 'w', encoding='utf-8').write(content)
new_len = len(content)
print(f"  New size: {new_len:,} chars")
print(f"  Total removed: {original_len - new_len:,} chars ({100*(original_len-new_len)/original_len:.2f}%)\n")

# ── Verification ──
print("=== VERIFICATION ===")
src_size = os.path.getsize(src)
dst_size = os.path.getsize(dst)
print(f"  File size: {src_size:,} -> {dst_size:,} bytes  {'PASS' if dst_size < src_size else 'FAIL'}")

# Check line 63 starts with const PAGES
lines = content.split('\n')
line63 = lines[62] if len(lines) > 62 else ''
print(f"  Line 63: {repr(line63[:60])}")
prefix_check = line63.startswith('const PAGES = {"home":')
print(f"  Line 63 starts with 'const PAGES = {{\"home\":': {'PASS' if prefix_check else 'FAIL'}")

# Check deityHerbs not in PAGES lines
pages_line = next((l for l in lines if l.startswith('const PAGES')), '')
has_deity = 'deityHerbs' in pages_line
print(f"  deityHerbs in PAGES line: {'FAIL (still present)' if has_deity else 'PASS (removed)'}")

has_summary_key = '\"summary\":\"' in pages_line
print(f"  summary as PAGES key: {'FAIL (still present)' if has_summary_key else 'PASS (removed)'}")
