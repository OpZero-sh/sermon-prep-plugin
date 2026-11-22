#!/bin/sh
# This cue is local. It never reads the tool payload or writes to disk.
cat <<'RESULT'
{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "Read the save result before reporting success. When the save succeeded, give the returned sermon title or ID and draft version. When it reported a version conflict, fetch the current draft and preserve both sets of edits."}}
RESULT
