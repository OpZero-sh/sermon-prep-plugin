#!/bin/sh
# Asks the pastor to confirm before a sermon is deleted.
# This script is local. It never reads the tool payload, writes to disk or uses the network.
cat <<'RESULT'
{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "ask", "permissionDecisionReason": "Sermon Prep is about to delete one sermon with its outline, its notes and every draft version. This cannot be undone. Export the sermon first if you want a copy. Approve only if you asked to delete this sermon."}}
RESULT
