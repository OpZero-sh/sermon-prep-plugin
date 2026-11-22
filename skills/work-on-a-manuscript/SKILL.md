---
name: work-on-a-manuscript
description: "Use when a pastor wants to start a sermon, save a draft or outline, retrieve an earlier version, or export a handout from saved material."
---

Locate the sermon with `list_sermons` and `get_sermon`. Use the exact sermon ID and current draft version. Start a new entry with `start_sermon` when requested.

For revisions, pass the current `base_version` to `save_draft` (zero for the first draft). If the server reports a conflict, fetch the latest draft and reconcile the intended changes before retrying. `save_outline` replaces the ordered outline; read the existing points before a partial edit. Preserve the pastor’s own text and identify prose the pastor asks Claude to write as `author: claude`. With `add_note`, attach the actual source of a quotation or returned DOI for a study.

For a handout, study notes or a small-group guide, call `export_sermon` with the chosen format. Return the text and its source labels. If a draft was saved, give its version so the pastor can get back to it.
