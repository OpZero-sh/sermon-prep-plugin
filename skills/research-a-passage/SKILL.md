---
name: research-a-passage
description: "Study a preaching text on the Sermon Prep passage desk: the passage by paragraph, the Greek or Hebrew word under an English word, ranked cross references, and where the early Church Fathers cite the verse. Use when a pastor or teacher is preparing to preach or teach a passage, wants to compare the BSB and KJV, asks about a word in the passage, wants cross references, or wants a patristic quotation with a citation. Typical requests: 'study John 15:1-5 with me', 'open the passage desk for Philippians 4:4-9', 'what is the Greek word for abide in John 15:4', 'cross references for Romans 8:28', 'which Fathers quote John 15:5'."
---

# Research a passage

Gather the evidence for a preaching text: the text itself, the words under it, related verses and early Christian citations. Every item carries its source. Interpretation and application belong to the pastor.

Three connectors are involved. The Sermon Prep desk needs sign in. Scripture Lookup and Church Fathers Library are public and read only.

## When to use

- A pastor names a passage to preach or teach.
- A question about a word in that passage, its cross references, or who among the Fathers cites it.

Use `plan-sundays` for the church year setting of a date, `read-the-fathers` to browse or read a patristic work that is not tied to one verse, `find-research` for outside studies, and `work-on-a-manuscript` to save anything.

## Tools

| Tool | Server | Use it for |
| --- | --- | --- |
| `study_passage` | Sermon Prep desk | Opens the passage desk: text by paragraph in the BSB or KJV, the word under each English word, cross references and Church Fathers citations. Up to 80 verses at a time. |
| `word_in_passage` | Sermon Prep desk | The Strong's entry for one word in the passage and the other verses that use the same Greek or Hebrew word |
| `cross_references` | Sermon Prep desk | Related verses with text, ranked, each marked with its source list |
| `fathers_on_passage` | Sermon Prep desk | Sections of the Ante-Nicene and Nicene and Post-Nicene Fathers that cite a verse, by volume and section |
| `compare_translations` | Scripture Lookup | BSB and KJV verse by verse, argument `reference` |
| `get_passage` | Scripture Lookup | Exact text of a reference, arguments `reference` and `translation` |
| `read_section` | Church Fathers Library | The text of a cited section, arguments `volume`, `section`, optional `page` and `notes` |

The desk tools sit behind sign in. Follow the argument names in each tool's schema at call time. The data sources behind each tool and their limits are in [references/sources-and-limits.md](references/sources-and-limits.md). Read it before telling a pastor that a source says nothing.

## Workflow

1. Settle the passage and translation. Call `study_passage` with the reference. If the passage runs past 80 verses, split it at a natural break and say so.
2. If wording matters, call `compare_translations` for the verses in question and set the differing words side by side.
3. For a word, call `word_in_passage`. Report the Strong's number, the lemma, the dictionary definition and the other verses returned. Keep the dictionary gloss apart from any reading of the passage.
4. For related verses, call `cross_references`. Keep the ranking and the source marks. Pick out the few that bear on the pastor's question and give the reason for each.
5. For early Christian use of the verse, call `fathers_on_passage`. Each hit names a volume and a section. Carry those identifiers over exactly and call `read_section` to read the text before quoting it. A citation of a verse is not yet an interpretation of it: read enough of the section to see how the writer uses the verse.
6. Return a small set of the strongest leads. Leave everything in the conversation until the pastor asks to save it.

## Decision points

- **Lectionary readings.** The data has the Sunday's name, season, colour and lectionary year, but no appointed readings. Do not infer readings from the season. Ask the pastor for the text.
- **No patristic hits.** The index is built from the scripture references printed in the edition. A writer who alludes to the verse without a printed reference is not found. Say that no printed citation was indexed, not that the Fathers are silent. Offer `read-the-fathers` to look in a commentary or homily series on that book.
- **A title match is not a citation.** Searching the library by title finds works and chapters, not discussions of a verse.
- **Attribution.** Report author and work as the edition gives them. If you know an attribution is disputed, say so and say that the point comes from outside the tool.
- **Drafting.** If the pastor asks for an outline or wording, treat that as a separate request under `work-on-a-manuscript`, where assistant writing is labeled as a suggestion. Do not volunteer an outline.

## Errors and empty results

- A sign in message from a desk tool: ask the pastor to connect and sign in to Sermon Prep. The public Scripture and Fathers tools still work meanwhile.
- An unknown book or a verse out of range: relay the message and ask for the reference again.
- An unknown volume or section in `read_section`: recheck the identifiers from `fathers_on_passage`. Do not guess a nearby section.

## What the answer looks like

For each lead: the quotation exactly as returned, kept short, then its source.

- Scripture: reference and translation.
- Word: Strong's number, lemma, definition as given, with the note that it is a dictionary entry of 1890.
- Cross reference: the reference, its text, the source mark, and one line on why it is relevant.
- Father: author or attributed work, title, book or chapter, series and volume, section id, and a sentence of context. Note that the English is a translation of the 1880s.

Mark any preaching suggestion as a suggestion, apart from the sources. Take no side between traditions.

## Examples

**"Study John 15:1-5 and find one early interpretation I can read in context."**
Call `study_passage` for John 15:1-5. Call `fathers_on_passage` for the verse the pastor cares about most, or for 15:5 if none is named. Choose a hit, call `read_section` with its volume and section, and return a short quotation with author, work, volume and section, plus two sentences on what the surrounding text is doing.

**"What is the word behind 'abide' in John 15:4, and where else does John use it?"**
Call `word_in_passage` for that word in that verse. Report the Strong's number, the lemma and the definition, then list the other verses returned. Say that the list is of verses using the same word, and leave conclusions about John's usage to the pastor.

**"Does anyone in the early church comment on Psalm 117?"**
Call `fathers_on_passage`. If nothing is indexed, say so in those terms and offer to look through Augustine's Expositions on the Psalms with `read-the-fathers`.
