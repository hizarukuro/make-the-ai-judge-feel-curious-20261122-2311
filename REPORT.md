# Report — Make the AI judge feel curious

## Final entry text

> Every night at half past three, the light comes on in the empty house down the lane. The curtains never stir. Yet it burns until dawn, and by morning the windows are dark again. Some nights I walk down to look. The key is still under the third stone. I have never turned it.

**Code-point count: 274** (within the required 1–280 range; target band 250–279).

## Verification

- `main.py` run twice with a clean environment (`env -i`) into two fresh
  output directories; both `entry.txt` outputs byte-identical.
- Count confirmed with `len()` on the string: 274 code points.
- One fragment edit applied after the first verification (wording
  improvement), then the two-run verification repeated: byte-identical,
  count still 274.
