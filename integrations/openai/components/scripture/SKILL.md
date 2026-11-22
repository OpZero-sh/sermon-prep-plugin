---
name: use-scripture
description: "Read a Bible passage, compare the BSB and KJV, or locate a remembered phrase. Use when someone asks what a verse says, wants a passage quoted exactly, remembers words but not the reference, or asks how the two translations differ."
---

Scripture Lookup is public and read only. It serves the Berean Standard Bible (BSB, the default) and the King James Version (KJV) and nothing else.

1. For a reference, call get_passage with reference and, when asked, translation set to KJV. References can be a verse (John 3:16), a range (John 3:16-18), a chapter (Psalm 23) or several places (Rom 8:28; 12:1-2). One call returns up to 200 verses.
2. For a wording question, call compare_translations with the reference. It returns both texts verse by verse.
3. For remembered words, call search_verses. Every word must appear in the verse, and an exact phrase goes in double quotes. Narrow with book or testament (OT or NT), raise limit up to 50, and page with offset. Show the matches, then fetch the one the person meant.
4. For questions about editions or licenses, call list_translations.

Quote the returned text word for word and give the reference and translation with every quotation, for example John 3:16 (BSB). Do not paraphrase inside quotation marks or add verses the tools did not return. If another translation is requested, say that only BSB and KJV are available and ask which to use. Do not present their wording as another edition.

If a search finds nothing, retry once with fewer words or in the other translation, then say the phrase was not found. An unknown book or a verse past the end of a chapter returns an error that names the problem. Relay it and ask again. A verse marked as not in the BSB main text should be reported as returned. Only the 66 book canon is covered.
