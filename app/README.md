# App Files

Place the current runnable single-file app builds in this folder.

## Current intended starting file

```text
greenman_v1_QUERY_FIRST_RESTORE_LAST_WORKING_SPELLBUILDER_v4.html
```

That file is currently stored in the ChatGPT workspace and should be uploaded here as the first runnable app checkpoint.

I could not safely upload the large HTML through the first GitHub setup step, so the repo has been prepared with the correct rules and structure first.

## Do not use as source

Do not use the broken all-pages-clean HTML as the master. It made pages visually clean but disconnected too much working logic.

## Recommended next commits

1. Add the last working v4 HTML into this folder.
2. Add extracted JSON/data files into `/src/data`.
3. Add engine files into `/src/engine`.
4. Rebuild one page at a time.
5. Export final single offline HTML back into `/app`.