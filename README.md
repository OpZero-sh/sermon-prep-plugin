# Sermon Prep

Build a sermon from the passage outward, with parallel translations, original-language notes, early Christian sources and a private place for the manuscript.

[Connect with Claude, ChatGPT, Muse Code, or Grok](PROVIDERS.md)

Trace a verse through the early church, read a paragraph on either side of a quotation, and carry its citation into your preaching notes. The passage desk keeps drafts by version. When you are ready for Sunday, turn saved material into a handout or small group guide.

The sermon stays yours. The tools save what you write and show every source. If you ask Claude to draft something, it is stored as a suggestion labeled as written by Claude.

## Try it

- “Study John 15:1-5 and find one early interpretation I can read in context.”
- “Find Ignatius’s letter to the Romans and read the first chapter.”
- “What are the next six Sundays in the church year?”
- “Show my most recent sermon on Romans and open its latest draft.”
- “Turn the saved notes for my sermon into a small group guide.”

## Get started in Claude

In Claude Code, run these commands in a session and reload plugins if prompted.

```text
/plugin marketplace add OpZero-sh/plugins
/plugin install sermon-prep@opzero
```

In Claude chat or Cowork, open the installed plugin’s Connectors tab and connect the public Scripture Lookup and Church Fathers Library services. Sign in to Sermon Prep to use the passage desk and your private sermon library.

## What is included

### Skills

| Skill | What it does |
| --- | --- |
| `research-a-passage` | Studies a preaching text on the passage desk: the text by paragraph, the Greek or Hebrew word under an English word, ranked cross references, and where the Church Fathers cite the verse. |
| `read-the-fathers` | Finds and reads a work in the Ante-Nicene and Nicene and Post-Nicene Fathers, with context and a full citation. |
| `find-research` | Finds peer reviewed studies on a theme, each with its DOI, and keeps them labeled as outside research, apart from Scripture. |
| `plan-sundays` | Lists the coming Sundays with church year name, season, colour and lectionary year, beside the books you have and have not preached. |
| `work-on-a-manuscript` | Starts a sermon, saves drafts by version, saves an outline and notes with their sources, exports a handout, study notes or small group guide, and deletes a sermon after you confirm. |

Each skill folder has a reference file with the data sources, limits and rules the skill relies on.

### Agent

`patristic-researcher` is a read only researcher. Given a verse, it looks up which Fathers cite it, opens the cited sections, reads around them, and returns short quotations with full citations and a record of what it could not confirm. It cannot read or change your sermons.

### Hooks

None. The plugin has no hooks and runs no code on your machine.

The `work-on-a-manuscript` skill carries the safeguards instead. After a draft is saved it tells Claude to read the save result before reporting success, to give you the sermon and draft version, and on a version conflict to fetch the current draft and keep both sets of edits. Before a sermon is deleted it tells Claude to ask you to confirm, because the deletion removes the sermon, its outline, its notes and every draft.

## What the plugin connects to and runs

The plugin talks to three remote MCP servers run by OpZero. It contacts no other host during normal use.

| Connector | Host | Sign in | What it receives |
| --- | --- | --- | --- |
| Sermon Prep | `sermon-prep.mcp.opzero.sh` | OpZero account | The passages, words and research themes you study, and the sermon titles, dates, drafts, outlines, notes and citations you choose to save |
| Church Fathers Library | `church-fathers-library.mcp.opzero.sh` | None | Title words, volume ids and section ids |
| Scripture Lookup | `scripture-mcp.mcp.opzero.sh` | None | Verse references and search words |

The two public services state that they do not store requests. Sermon Prep stores what you save under your account until you delete it. Its privacy policy says it does not log the passages you study or the themes you search. To answer a study request, the Sermon Prep service itself asks other services for public data: its sibling OpZero services receive the passage, word or date, OpenAlex receives a research theme you search, and the DOI registry receives the DOI of a study you save. The policy says none of them receives your name, your account or your sermon. Exports are returned to you in Claude and are not sent anywhere.

The repository also holds settings files for other assistants. Claude does not run them, and nothing in the plugin calls them. The two scripts that use them are not in this repository. They live in the catalog repository, [OpZero-sh/plugins](https://github.com/OpZero-sh/plugins).

- The catalog's `tools/build_openai.py` builds ZIP packages for ChatGPT and Codex from this repository's skills, license, `assets/icon.png` and `integrations/openai`. It reads local files and writes ZIP files to the folder you name. It uses no network.
- The catalog's `tools/grok_example.py` is an optional example for the xAI API. It reads `integrations/grok-servers.json` and `XAI_API_KEY` from your environment, and for the Sermon Prep connection an access token from `SERMON_PREP_ACCESS_TOKEN`, and sends one request to `api.x.ai` only when you run it yourself without the dry run flag. With the dry run flag it prints the request and sends nothing.
- The JSON files under `integrations/` are settings for those assistants. They list the same three hosts.

## Sources and limits

- Bible text: Berean Standard Bible and King James Version, 66 book canon.
- Words: STEP Bible tagging (CC BY 4.0) and Strong’s dictionary of 1890.
- Cross references: Treasury of Scripture Knowledge with data from OpenBible.info.
- Church Fathers: the Ante-Nicene Fathers and Nicene and Post-Nicene Fathers from the Christian Classics Ethereal Library, in English translations of the 1880s. Title search only. The verse index covers scripture references printed in the edition, so an allusion without a printed reference is not found.
- Church year: computed from the Easter rules, following common Western usage. Lectionary readings are not included.
- Research: citations and abstract excerpts from OpenAlex. Not medical, psychological or legal advice.
- The plugin is a study aid. It is not a counseling or crisis service.

## In use

Examples from the connected services in Claude.

![Searching for the Eucharist in the Didache](media/didache.webp)
