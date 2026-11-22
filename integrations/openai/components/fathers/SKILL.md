---
name: use-fathers
description: "Locate and read a work from the Ante-Nicene or Nicene and Post-Nicene Fathers and cite it. Use when someone names a Father or a work, asks what a volume contains, or wants the context around a patristic quotation."
---

Church Fathers Library is public and read only. It holds 38 volumes in English translations of the 1880s: the Ante-Nicene Fathers (anf01 to anf10) and the Nicene and Post-Nicene Fathers, Series 1 (npnf101 to npnf114) and Series 2 (npnf201 to npnf214).

1. Find the work. Call find_sections with a few title words, such as Ignatius Romans or Confessions Book VIII, using a Roman numeral for a book or chapter. It matches section titles, not the body text, so a verse reference or a topic usually returns nothing. If the title search fails, call list_volumes to choose a volume and volume_contents (depth 1 to 3, offset for paging) to walk its headings.
2. Read it. Call read_section with the volume id and the section id exactly as returned, including capital letters. Long sections come in pages of about 6000 characters, and the last line gives the page count and the previous and next section ids. A top section may hold only a title, so follow the next section link. Set notes to true for the translators' and editors' footnotes.
3. Read enough around a quotation to see what the writer is arguing before describing it.

Quote sparingly and exactly as returned, leaving the older English as it stands. Cite the author, the work with its book and chapter, the series and volume, and the section id. Search the edition's own titles: the Didache is listed as The Teaching of the Twelve Apostles in anf07. Where the edition prints more than one version of a work, as with the shorter and longer versions of Ignatius, which follow one another in the same section without labels, say which version is quoted. Give attributions as the edition does and mark anything you add about disputed authorship as coming from outside the tool. Do not present one writer as speaking for the whole early church.

An unknown volume or section returns an error. Go back to list_volumes, volume_contents or find_sections for a valid id and do not guess.
