# GREENMAN CHANGE LOG - SPELL TO CANDLE FIX v2

Base file used: `Spell_app_v1_correct_styling_EMPTY_BOWL_REPAIR_v1_ANDROID_VIEW_FIX2.html`
Output file: `Spell_app_v1_correct_styling_EMPTY_BOWL_REPAIR_v2_SPELL_TO_CANDLE_FIX.html`

## Issue reported
Spell names now appear correctly in Spell List, but tapping a spell does not move to the Candle page.

## Exact code changed
Embedded page: `PAGES.spellList` only.
Function changed: `selectSpell(name, phase)` only.

## Original code changed

```js
  var n=document.getElementById('selected-note');
  n.innerHTML='Selected: '+escapeHtml(name)+' &middot; Next: Candle';
  n.style.display='block';
  setTimeout(function(){n.style.display='none';},1700);
}
document.addEventListener('DOMContentLoaded', renderSpellList);
```

## New code used

```js
  var n=document.getElementById('selected-note');
  n.innerHTML='Selected: '+escapeHtml(name)+' &middot; Next: Candle';
  n.style.display='block';
  setTimeout(function(){n.style.display='none';},700);

  /* EMPTY BOWL REPAIR v2:
     This page now sends the selection and navigation itself.
     Reason: the dynamic spell buttons are rendered by this page, so the old shell bridge wrapper was not reliably carrying the tap through to Candle on Android.
     This directly updates the parent shell without adding a second route layer. */
  try{
    parent.postMessage({
      source:'greenman-new-shell-v1',
      cmd:'spellSelected',
      page:'spellList',
      spell:name,
      moonPhase:phase
    }, '*');
    setTimeout(function(){
      parent.postMessage({
        source:'greenman-new-shell-v1',
        cmd:'nav',
        page:'spellList',
        target:'candle'
      }, '*');
    }, 120);
  }catch(e){}
}
document.addEventListener('DOMContentLoaded', renderSpellList);
```

## Not changed
- Candle logic
- Category logic
- Selection pages
- Tracker
- Moon / Planets / Hours
- Journal / BoS / Grimoire
- Print Pack

## Reason this is not double-stacking
This changes the existing `selectSpell` function directly inside `PAGES.spellList`. It does not add a new shell, duplicate route system, extra overlay, duplicate tracker, or hidden second button.
