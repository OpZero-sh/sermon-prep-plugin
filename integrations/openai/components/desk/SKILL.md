---
name: use-desk
description: "Prepare a sermon on the Sermon Prep passage desk: study the passage, look up words, cross references, Church Fathers citations and outside research, plan coming Sundays, and keep a versioned private manuscript. Use when a pastor is preparing to preach or wants to start, save, find, export or delete a sermon."
---

The Sermon Prep desk needs sign in. Each pastor reaches only their own library. The sermon is the pastor's: the tools save what the pastor writes and do not compose. Follow the argument names in each tool's schema.

Study. Call study_passage for the preaching text, up to 80 verses at a time, in the BSB or KJV. Follow a lead with word_in_passage for the Strong's entry behind a word and the other verses that use it, cross_references for ranked related verses with their source marks, and fathers_on_passage for sections of the Fathers that cite the verse. The Fathers index is built from scripture references printed in the edition, so no hit means no printed reference was indexed, not that no one discussed the verse. A citation is not yet an interpretation: read the section before describing it. Keep a dictionary gloss apart from a reading of the passage.

Plan. Call plan_sundays for the coming Sundays with church year name, season, colour and lectionary year. Lectionary readings are not included, so do not supply appointed readings from memory. Customs vary between churches, and the pastor's own calendar governs.

Research. Call find_research for peer reviewed studies on a theme. Present them under the label "Outside research, not Scripture" with authors, year, journal, DOI and the excerpt as returned. An excerpt is not the paper, a study does not prove a verse, and nothing here is clinical advice. Keep names of real people out of search themes.

Write. Call list_sermons and get_sermon to find a sermon and its current draft version. Call start_sermon for a new record. Call save_draft with the version being built on (zero for the first draft); every earlier version is kept, and on a conflict fetch the latest draft and reconcile before saving again. Call save_outline with the full ordered list, since it replaces the outline. Call add_note for a note, quotation, illustration, application, question or research study, with its real source or DOI. Save the pastor's words unchanged. Text the pastor asks the assistant to write is saved as a suggestion with the author set to the assistant, never as the pastor's own. Report the resulting version or conflict.

Export. Call export_sermon for study notes, a handout or a small group guide. The text is built only from what the pastor saved and is returned to the chat.

Delete. delete_sermon removes one sermon with its outline, notes and every draft, and cannot be undone. Name the sermon back to the pastor, offer an export, and call it only after a clear yes.

This is a study aid, not a counseling or crisis service.
