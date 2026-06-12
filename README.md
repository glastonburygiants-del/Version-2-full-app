# Greenman HedgeWitchery Spell App — Version 2 Full App

This repository is the clean rebuild workspace for the Greenman HedgeWitchery app.

## Current safe starting point

The current runnable starting file is:

```text
app/greenman_v1_QUERY_FIRST_RESTORE_LAST_WORKING_SPELLBUILDER_v4.html
```

This is the last known working query-first spell-builder version restored after the later all-page cleanup broke too much.

## Build rule

Do not patch random parts of the old giant shell without logging the change.

Work in small stages:

1. Keep the working spell-builder safe.
2. Fix one page or system at a time.
3. Test on phone after each change.
4. Only then move to the next page.

## Main goal

Turn the old giant shell into a query-first app:

- visual pages are empty bowls
- JSON/data holds real item records
- the engine filters and ranks choices
- tracker reads the single state
- summary, altar, Journal, BoS and Print Pack read the same state

## Do not use

Do not use the broken all-pages-clean version as the source. It removed too much working logic and left placeholder pages.