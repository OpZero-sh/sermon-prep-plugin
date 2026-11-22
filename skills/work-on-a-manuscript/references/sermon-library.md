# The sermon library: what is stored, versions, authorship and exports

Facts in this file come from the published guide and privacy policy of the Sermon Prep server at https://sermon-prep.mcp.opzero.sh/?page=docs, and from the tool descriptions on that page. The desk tools require sign in. Follow each tool's own schema for argument names and treat the schema as correct where it differs from this file.

## Sign in

Sermon Prep uses OpZero accounts through OAuth. Each signed in pastor can reach only their own library. To keep a library the pastor confirms they are 13 or older and accepts the service's privacy policy and terms.

## What a sermon record holds

| Part | Saved by | Notes |
| --- | --- | --- |
| Title, passage, preaching date, series | `start_sermon` | The record everything else attaches to |
| Draft | `save_draft` | Each save is a new version. Every earlier version is kept. |
| Outline | `save_outline` | Ordered points with references. A save replaces the previous outline. |
| Notes | `add_note` | One of: note, quotation, illustration, application, question, research study |

For each saved item the service records when it was saved and whether the pastor or the assistant wrote it.

## Authorship

The service's published commitment is that no tool composes a manuscript and that the writing tools save what the pastor writes. If a pastor asks the assistant for a draft, the text is labeled as written by the assistant and stored as a suggestion, never as the pastor's text. `get_sermon` marks such text as a suggestion when it returns it.

In practice:

- Pass the pastor's words unchanged and as theirs.
- Pass assistant prose with the author set to the assistant.
- Do not mix the two in one save without telling the pastor which parts are which.
- Do not relabel a suggestion as the pastor's own. If the pastor rewrites it in their own words, save their rewrite as theirs.

## Versions and conflicts

- A draft save names the version it builds on. The first draft builds on zero.
- If the stored draft has moved on since that version, the server reports a conflict and does not save. Fetch the latest draft, reconcile the two sets of changes with the pastor, and save on the new base.
- Because every version is kept, a save never destroys earlier text. An outline save does replace the earlier outline.

## Exports

`export_sermon` returns plain text in one of three formats:

| Format value | Output |
| --- | --- |
| `study_notes` | Study notes |
| `handout` | A handout |
| `small_group_guide` | A small group guide |

The export is built only from what the pastor saved, with every citation. It is returned to the chat. Nothing is posted, sent or published. The same exports are available on the service's web page when signed in.

## Deleting

- `delete_sermon` removes one sermon with its outline, notes and every draft version.
- The privacy policy says the library is kept until the pastor deletes it. To delete everything at once, the policy directs the pastor to write to the service from the address they sign in with. There is no tool for deleting the whole library.
- The tools offer no restore. An export or a copy of the draft taken beforehand is the only backup.

## Shared counts

When a pastor adds a cross reference or a research study to a sermon, the service adds one to a shared count for that reference or that study's DOI, so that lists can show which ones pastors keep. The policy describes the count as a number that holds no text, no sermon and no name. Mention this if a pastor asks what leaves their account.

## What the service says about privacy

- It stores only what the pastor chooses to save, under the account identifier from sign in.
- It does not save or log the passages studied, the words looked up or the research themes searched.
- Sermon drafts and notes can reveal faith and details of a congregation. The policy says they are kept to the account, never used for advertising, never sold, never used by the service to train models and never shared.
- Illustrations and notes may mention members of a congregation. That is the pastor's judgment to make. Do not add names or personal details the pastor did not supply.

Point the pastor to the policy itself for anything beyond these statements.

## Responsibility for the result

The service's terms say the pastor is responsible for what is preached and published, and for checking any quotation or study against its source before use. Keep citations attached to quotations through every save and export so that check stays possible.
