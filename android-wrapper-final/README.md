# Greenman HedgeWitchery Android wrapper

This project packages the exact supplied `GREENMAN_HEDGEWITCHERY.html` inside a thin native Android WebView shell.

## Protected baseline

- HTML SHA-256: `f4d982d048514bb9aaae6f6858240d6eb61619ba024d571e8a0ed3b43ce07fba`
- No HTML, CSS, JavaScript, page styling, button styling, embedded page content, or app data was rewritten.
- The Android layer supplies only the launcher icon, fullscreen window, persistent WebView storage, local secure-origin asset loading, Android file picking, offline export saving, native print handoff, and basic physical Back handling.
- External navigation is blocked. The APK does not request Internet permission.

## Build

Requires Java 17, Gradle 8.9, Android SDK Platform 35 and Build Tools 35.0.0.

```bash
gradle :app:assembleDebug
```

The installable test APK is created at:

`app/build/outputs/apk/debug/app-debug.apk`
