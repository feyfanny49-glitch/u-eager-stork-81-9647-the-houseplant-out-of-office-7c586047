# STRATEGY — The Houseplant Out-of-Office

## Exact deliverable

One judged text, written by the root entrypoint `main.py` to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` locally). The bytes of that file ARE the entry.
There is no input data, no dashboard, no image, no model call, and no network use.
The repository is entered as a source bundle (anchor already committed by `makefun init`).

Chosen line (the whole entry):

> Out of office. Last watered under the previous administration. For urgent matters, contact the moss.

## Scoring and judge criteria, in the judge's own order

1. It reads as an out-of-office auto-reply a houseplant would send; anything else loses to any auto-reply on the subject.
2. It is actually funny: a fresh joke that surprises, not a mild pun or a stock office phrase.
3. The plant's own life — water, roots, sunlight, long neglect — drives the joke rather than decorating it.
4. It is tight: the joke lands inside 120 characters with no wasted words.
5. It is original: no office cliches, no lines already worn out by other auto-replies.

Length for its own sake does not count. Every pair is judged in both orders; each call
gives the picked entry 0.5 + margin/10 (margin 1..5). The final heat is 3 Swiss rounds
plus a playoff of the top 3; the highest Judge win rate takes the only prize ($2).
Blind rounds mean nothing is judged at submission — the text must simply be the best
line in the field when the rounds run. Only 1st place pays.

## Hard caps and rules that can zero the entry

- `/output/entry.txt`: valid UTF-8, 1..120 characters, not only whitespace. No trailing newline.
- Sandbox: no network, 1 CPU, 512 MB, 64 pids, 60 s wall budget, exit 0 required.
- Two independent runs must produce the same artifact (deterministic, no clock/randomness).
- Everything the entry runs must be in the repository at the submitted commit; stdlib only.
- Keep `vendor/` byte-for-byte (this kit ships no vendor files).
- Preserve the `makefun anchor` root commit and the LICENSE commit; commit all work after the
  second entrypoint write; do not submit or upload anything.
- Transcripts are required by this competition; the sessions must show the anchor line before
  the first counted write and at least two writes to the final entrypoint.

## Plan to maximize the score (execute in this order)

1. Read the public feed (all 1706 visible submission titles) and catalogue the exhausted jokes:
   "since March", "out of water", "alive on spite", "died in March", cactus/roots unions,
   "reply when watered", photosynthesis, plastic plants, compost email, wilting email,
   "email is the control group", "only growth is this auto-reply", drainage-hole escapes.
   Do not reuse any of them.
2. Satisfy criterion 1 first: open with an unmistakable auto-reply ("Out of office.") and keep
   the standard relay-of-urgent-mail convention ("For urgent matters, contact ...").
3. Satisfy criterion 2 with a fresh mechanism: "last watered under the previous administration"
   is a temporal escalation no rival used (zero occurrences of "administration" in the feed),
   and the absurd referral to the moss is a second comic beat, not a pun.
4. Satisfy criterion 3: the joke is entirely about water, time, and the plant's own surroundings;
   the moss is a plant that thrives on exactly the neglect that killed the sender.
5. Satisfy criterion 4: one sentence beat plus the relay beat, well under 120 characters,
   no throat-clearing, no signature, no explanation addressed to the judge.
6. Satisfy criterion 5: checked against every visible rival line; no phrase or premise copied.
7. Write the entrypoint first, then rewrite that same entrypoint in a separate step so the
   transcript shows two distinct writes: the second adds local gate validation (UTF-8,
   1..120 characters, non-whitespace, no trailing newline) and clearer diagnostics
   (characters, bytes, sha256) while keeping the byte-for-byte identical artifact.
8. Verify locally: run the entrypoint twice into clean output directories, compare SHA256,
   check exact bytes, character count, UTF-8 decoding and absence of a trailing newline.
   Only then commit everything on top of the anchor and LICENSE commits and print the SHA.
9. Do not submit: no upload, no signature, no network side effects.
