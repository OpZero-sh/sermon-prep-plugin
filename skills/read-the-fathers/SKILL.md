---
name: read-the-fathers
description: "Find and read a work of the early Church Fathers in the Ante-Nicene Fathers and Nicene and Post-Nicene Fathers, and cite it properly. Use when someone names a Father or a work and wants to read or quote it, asks what a volume contains, or wants the context around a patristic quotation. Typical requests: 'find Ignatius to the Romans and read the first chapter', 'show me Augustine Confessions book 8', 'what does the Didache say about the Eucharist', 'what is in NPNF series 2 volume 4', 'read the next section', 'include the footnotes'."
---

# Read the Fathers

Locate a work in the Church Fathers Library and read it section by section. The connector is public, read only and needs no sign in. It holds the 38 volumes of the Ante-Nicene Fathers and the two series of the Nicene and Post-Nicene Fathers in their English translations of the 1880s.

## When to use

- A Father, a work, or a chapter is named.
- A quotation needs its surrounding context or a citation.
- Someone wants to see what a volume or a series holds.

Use `research-a-passage` when the starting point is a Bible verse and the question is who cites it. This library searches titles, not the full text, so it cannot find every place a verse or a topic is discussed.

## Tools

All four are on the Church Fathers Library server.

| Tool | Use it for | Arguments that matter |
| --- | --- | --- |
| `list_volumes` | The volumes and the Fathers each covers | optional `series`: `all`, `anf`, `npnf1`, `npnf2` |
| `find_sections` | Works, books and chapters whose titles match | `query` (title words), optional `volume`, optional `limit` (1 to 30, default 12) |
| `volume_contents` | The works and sections of one volume | `volume`, optional `depth` (1 to 3, default 2), optional `offset` for paging |
| `read_section` | The text of one section | `volume`, `section`, optional `page` (default 1), optional `notes` (true to include translator and editor footnotes) |

Volume ids, where the major writers are found, section ids and a citation template are in [references/library-map.md](references/library-map.md). Read it when choosing a volume or writing a citation.

## Workflow

1. Find the work.
   - If the author and title are known, call `find_sections` with a few title words, for example `Ignatius Romans` or `Confessions Book VIII`. Use a Roman numeral for a book or chapter number.
   - If the title search returns nothing, pick the volume from the library map or from `list_volumes` and call `volume_contents` on it. Start at `depth: 1` for a large volume, then go deeper.
2. Choose the section. Results give a volume id and a section id such as `v.v`, `viii.iii.ix` or `vi.VIII`. Use them exactly as returned, including capital letters.
3. Call `read_section`. Long sections come in pages of about 6000 characters. The last line of each result gives the page count and the ids of the previous and next sections. Read further pages or neighbouring sections until you have the context the question needs.
4. Set `notes: true` when the footnotes matter. They carry the translators' scripture references and textual remarks.
5. Answer with a short quotation and a full citation.

## Decision points

- **A heading with no text.** The top section of a work is often only its title. Follow the next section link to reach the first chapter.
- **Several versions of one work.** The edition prints some works in more than one form. For the letters of Ignatius it prints the shorter and longer versions one after the other in each section, unlabeled, and a Syriac version separately. Say which version a quotation comes from. See the library map.
- **Two works with similar titles.** A title search can return different works. The Teaching of the Twelve Apostles in ANF 7 is the Didache. The Teaching of the Apostles in ANF 8 is another document. Check the volume and the opening lines before quoting.
- **A title you know by another name.** Search the edition's title. The Didache, for example, is listed as The Teaching of the Twelve Apostles.
- **A question about a topic or a verse.** A title search will not find it. Say so, then suggest a work likely to treat it, or use `research-a-passage` for verse citations.
- **Attribution and date.** Give the author as the edition does. Add what you know about disputed authorship only when it matters, and mark it as coming from outside the tool.

## Errors and empty results

- No title matches: the server suggests fewer words, a Roman numeral, or naming the volume. Try each once, then browse with `volume_contents`.
- Unknown volume: ids look like `anf01`, `npnf101` or `npnf214`. Call `list_volumes` to see all 38.
- Unknown section: go back to `volume_contents` or `find_sections` for a valid id. Do not guess.

## What the answer looks like

- The quotation exactly as returned, kept to what the point needs. The older English stays as it is.
- Citation: author, work, book and chapter, then series and volume, then the section id so the passage can be found again.
- One or two sentences of context: who is being addressed and what the surrounding argument is.
- A note that the English is a translation of the 1880s when wording carries weight. For close work the pastor should check a modern translation or the original.
- Present the writer's words as a historical source. Do not treat one Father as speaking for all, and do not rank traditions by how they receive him.

## Examples

**"Find Ignatius's letter to the Romans and read the first chapter."**
Call `find_sections` with `query: "Ignatius Romans"`. Two entries in ANF 1 come back: the shorter and longer versions together at section `v.v`, and the Syriac version. Call `read_section` on `v.v`, which holds the salutation, then follow the next section link to chapter 1. Each chapter gives the shorter version first and the longer second, with no label between them. Quote the shorter version and name it.

**"What does the Didache say about the Eucharist?"**
The work is in ANF 7 under The Teaching of the Twelve Apostles. Call `find_sections` with that title and `volume: "anf07"`, then `volume_contents` at `depth: 3` to find the chapter on the Thanksgiving, and call `read_section` on it. Quote briefly and cite the chapter, ANF 7 and the section id.

**"What is in the fourth volume of the second series?"**
Call `volume_contents` with `volume: "npnf204"` and `depth: 1`. List the works of Athanasius it holds.
