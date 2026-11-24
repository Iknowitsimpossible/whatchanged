# WhatChanged

**Live site:** https://iknowitsimpossible.github.io/whatchanged/

AI writing tools rewrite your text but don't tell you what they changed. WhatChanged does. Paste your original text and the AI-edited version, and every removed word is highlighted in red and every added word in green, like a GitHub code review.

## Features

- **Split view**: original on the left, AI version on the right
- **Unified view**: one column with inline strikethroughs, like Word's track changes
- **Word or character mode**: words for rewrites, characters for typo and punctuation fixes
- **Stats**: words added, words removed, and how much of the original was kept
- Runs entirely in your browser. Your text is never uploaded anywhere.


## How it works

1. **Tokenize**: split each text into words (with their trailing spaces) or single characters.
2. **Diff**: find the longest common subsequence (LCS) of tokens with dynamic programming. Tokens in the LCS are unchanged; the rest of the original was deleted and the rest of the revision was inserted.
3. **Clean up**: merge small unchanged gaps between edits so a rewritten sentence shows as one red block and one green block instead of a word-by-word mix.
4. **Render**: build the highlighted output with `textContent`, so pasted HTML is shown as text and never executed.

The LCS table is n × m, so the page trims the shared start and end of both texts first and caps the table size. That handles roughly 7,000-word texts.
