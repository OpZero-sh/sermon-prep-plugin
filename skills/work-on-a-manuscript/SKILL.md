---
name: work-on-a-manuscript
description: "Keep a pastor's sermon in the private Sermon Prep library: start a sermon, save a draft as a new version, save an outline, attach notes and quotations with their sources, reopen earlier work, export a handout, study notes or small group guide, or delete a sermon. Use when a pastor wants to start, save, find, revise, export or delete a sermon. Typical requests: 'start a sermon on Psalm 23 for this Sunday', 'save this draft', 'show my most recent sermon on Romans', 'save this outline', 'add that quotation as a note', 'turn my saved notes into a small group guide', 'delete that sermon'."
---

# Work on a manuscript

Save and retrieve the pastor's own work on the Sermon Prep desk. The desk needs sign in, and each pastor can reach only their own library.

The sermon is the pastor's. These tools save what the pastor writes. They do not compose. Two rules follow:

1. Save the pastor's words as given. Do not polish, shorten or extend them unless asked.
2. Anything you write at the pastor's request is saved as a suggestion and labeled as written by the assistant, never as the pastor's text.

## When to use

- Starting a sermon record, or finding one already saved.
- Saving a draft, an outline or a note.
- Exporting saved material.
- Deleting a sermon.

Use `research-a-passage`, `read-the-fathers` and `find-research` to gather material. Nothing from those skills is saved until the pastor asks.

## Tools

All are on the Sermon Prep desk.

| Tool | Effect |
| --- | --- |
| `list_sermons` | Read only. The pastor's sermons, newest first, with which books have been preached and which have not. |
| `get_sermon` | Read only. One sermon with its latest draft, outline and notes. |
| `start_sermon` | Creates a sermon with title, passage, preaching date and series. |
| `save_draft` | Saves a new version of the draft. Every earlier version is kept. |
| `save_outline` | Saves the outline as ordered points with references. It replaces the outline that was there. |
| `add_note` | Adds a note, quotation, illustration, application, question or research study. |
| `export_sermon` | Read only. Returns study notes, a handout or a small group guide as plain text with every citation. |
| `delete_sermon` | Deletes one sermon with its outline, notes and every draft. |

The desk tools sit behind sign in, so follow the argument names in each tool's schema at call time. What the desk stores, how versions and authorship labels work, and the export formats are in [references/sermon-library.md](references/sermon-library.md).

## Workflow

**Find.** Call `list_sermons`, then `get_sermon` with the exact sermon id. Note the current draft version from the result. You need it before any save.

**Start.** Call `start_sermon` when the pastor asks for a new sermon. Pass the title, passage, preaching date and series they give. Ask for the passage if it is missing. Do not invent a title.

**Save a draft.**
1. Call `get_sermon` first unless you already hold the current version from this conversation.
2. Call `save_draft` with the full text and the version you are building on as `base_version`. Use zero for the first draft.
3. Mark who wrote the text. The pastor's own words are theirs. Prose the pastor asked you to write is saved with the author field set to the assistant, `author: claude`, so the desk stores it as a suggestion.
4. Read the result before reporting. On success give the sermon title or id and the new version number. On a version conflict, call `get_sermon` for the latest draft, show the pastor what changed, combine both sets of edits with their agreement, and save again on the new base.

**Save an outline.** `save_outline` replaces the whole outline. For a partial change, read the current points with `get_sermon`, apply the change, and send the full ordered list back.

**Add a note.** Call `add_note` with the kind of note and its text. For a quotation attach its real source: the Scripture reference and translation, or the Father, work, volume and section. For a research study attach the DOI that `find_research` returned. Do not save a quotation whose source you have not seen in a tool result.

**Export.** Call `export_sermon` with the sermon id and the format: study notes, handout or small group guide. The text is built only from what the pastor saved. Return it with its source labels intact. Nothing is posted or sent anywhere.

**Delete.** Deleting removes the sermon, its outline, its notes and every draft version, and these tools offer no way to restore it. Name the sermon back to the pastor with its title, passage and date, offer an export first, and ask for a clear yes. Then call `delete_sermon` with the sermon id.

## Decision points

- **Several sermons match.** List them with date, title and passage and ask which one.
- **"Write it for me."** You may draft at the pastor's request. Show the draft in the chat, say it will be stored as a suggestion labeled as written by the assistant, and save only when asked. Do not present assistant text as the pastor's own in the library or in an export.
- **A partial edit to a long draft.** `save_draft` stores the full text as a new version. Apply the change to the latest text and save the whole draft. Earlier versions stay available.
- **A quotation from memory.** Look it up first with the Scripture or Fathers tools. If it cannot be found, save it only as the pastor's own note and say the source is unverified.

## Errors and empty results

- A sign in message: ask the pastor to connect and sign in to Sermon Prep, then retry.
- No sermons yet: say so and offer to start one.
- An unknown sermon id: call `list_sermons` again. Do not guess an id.
- A version conflict on save: follow the conflict steps above. Never overwrite by retrying with a higher number.

## What the answer looks like

- After a save: the sermon title or id, what was saved, and the draft version, so the pastor can return to it.
- After an export: the exported text as returned, with its citations.
- After a delete: one sentence naming the sermon removed.

Keep comments on the content of a sermon to what the pastor asks for.

## Examples

**"Show my most recent sermon on Romans and open its latest draft."**
Call `list_sermons`, pick the newest whose passage is in Romans, and call `get_sermon` with its id. Give the title, date, draft version and the draft text.

**"Save this as the next draft."** followed by the pastor's text.
Call `get_sermon` for the current version, then `save_draft` with the pastor's text unchanged and that version as `base_version`. Report the new version number.

**"Turn the saved notes for my sermon into a small group guide."**
Find the sermon, then call `export_sermon` with the small group guide format. Return the text with its source labels.
