# Instruction pages: A4 lock removed (Journal + BoS)

Date: 2026-08-09

## Problem reported

The Instructions pages (page 3 of 4 and 4 of 4) inside the Journal's Book of
Shadows viewer and inside the standalone BoS tab were being forced into a
fixed A4-sized box (794x1123px on screen, 210mm x 297mm at print). When the
instruction text did not fit, an aggressive shrink loop pushed font sizes
down toward 6.4px trying to cram everything onto one sheet, producing
unreadably tiny text and clipped/bleeding content on longer entries.

The Print Pack (`PAGES.printPack`, the separately hand-tuned A4 print
system) was NOT touched. It already fits A4 correctly and was explicitly
out of scope for this fix.

## Cause found

- `PAGES.journal` (source line ~2273 onward) built each Instructions page
  through `buildInstructionPage()` -> `pageFrame(..., 'instructions-page')`,
  which reused the same `.a4-page` CSS as Summary/Altar: fixed
  794x1123px / 210mm x 297mm, `overflow:hidden`.
- A `fitInstructionText()` routine then shrank `.gm-making-text` /
  `.gm-voice-text` font-size in 0.36px steps (up to 32 iterations) whenever
  content overflowed that fixed box, both on screen (`renderActiveEntry`)
  and at print time (`printHtml`).
- `PAGES.bos` (source line ~2938 onward) shared the same fixed-size
  `.a4-page` / `.instruction-box` CSS (no font-shrink loop there, but the
  same `overflow:hidden` clipping risk).

## Fix applied

In both `PAGES.journal` and `PAGES.bos` only:

- Added a scoped CSS override for `.a4-page.instructions-page` (and its
  `.a4-content`, `.instruction-box`, `.gm-ritual-grid`, `.gm-step`
  descendants): `position:relative` (was `absolute`, so the decorative
  `.border-outer`/`.border-inner` insets still anchor correctly),
  `height:auto`, `overflow:visible`. Width is untouched, so the page still
  reads like an A4 sheet, it just grows downward with content instead of
  being clamped.
- Added the equivalent `@media print` override so printed Instructions
  pages are no longer forced to exactly 297mm / `overflow:hidden`; they
  flow naturally (with `page-break-before:always` so each Instructions
  page still starts on its own sheet, and `page-break-inside:avoid` on
  each step row).
- Removed the two `fitInstructionText()` call sites in `PAGES.journal`
  (`renderActiveEntry`, `printHtml`) since nothing needs shrinking once the
  box can grow. Left the function defined but unused (dead code, zero
  risk) rather than deleting it.
- Summary and Altar pages, and everything under the Print Pack section,
  were not touched.

## Verification

Loaded the file with Playwright (Chromium), injected a saved spell entry
into `localStorage.gm_journal_entries` with a heavy load (8 spell herbs),
and rendered the Instructions pages via both the Journal's "Book of
Shadows" sub-tab and the standalone BoS tab:

- Screen: Instructions page now renders at natural font size
  (11.2-12.1px, same as the CSS defaults) instead of the shrunk ~6.4px
  floor; no clipped text.
- Print (`page.emulateMedia('print')` + `printCurrentEntry()`):
  Summary/Altar pages measured unchanged at 297mm equivalent
  (`height:1122.52px`, `overflow:hidden`). Instructions pages measured
  `height:auto` (798px / 1146px for the two pages), `overflow:visible`.
- `git diff` confirms every changed line sits between source lines
  ~2387-2996, i.e. entirely inside `PAGES.journal` / `PAGES.bos`. Nothing
  in the Print Pack section (source line ~7452 onward) changed.

## Output file

- `greenman_v1_QUERY_FIRST_RESTORE_LAST_WORKING_SPELLBUILDER_v4.html`
  (edited in place)
