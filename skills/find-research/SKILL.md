---
name: find-research
description: "Find peer reviewed studies on a theme for a sermon or lesson, each with authors, year, journal, DOI and a short abstract excerpt, and keep them clearly apart from Scripture. Use when a pastor wants outside research, a study to cite, or evidence behind a claim they plan to make. Typical requests: 'find research on gratitude and wellbeing', 'is there a study on loneliness among older adults', 'what does the research say about forgiveness', 'save that study to my sermon'."
---

# Find research

Search for published studies on a theme with the Sermon Prep desk and present them as outside research, never as Scripture and never as advice. The desk needs sign in.

## When to use

- A pastor wants a study to cite, or wants to check whether a claim has support in published research.
- A pastor wants to save a study to a sermon.

Use `research-a-passage` for the biblical text and the Fathers. Do not use this skill to answer a personal medical, psychological or legal question. It finds citations for a sermon. It does not give guidance for a person's care.

## Tools

| Tool | Server | Use it for |
| --- | --- | --- |
| `find_research` | Sermon Prep desk | Peer reviewed studies on a theme, reviews first, each with DOI and a short abstract excerpt |
| `add_note` | Sermon Prep desk | Saving a chosen study to a sermon as a research note, with its DOI |
| `get_sermon`, `list_sermons` | Sermon Prep desk | Finding the sermon to attach a study to |

The desk tools sit behind sign in, so follow the argument names in each tool's schema at call time. Where the records come from, what the service promises about them and how to cite them are in [references/outside-research.md](references/outside-research.md).

## Workflow

1. Turn the pastor's question into a short theme of a few plain words, such as "gratitude wellbeing" or "loneliness older adults". Say what theme you searched. The theme is sent to an outside index, so keep names and details of real people out of it.
2. Call `find_research` with the theme.
3. Read what came back. Review articles are listed first. For each study worth showing give the authors, year, journal, DOI and the abstract excerpt as returned.
4. Say what the excerpt supports and what it does not. An abstract excerpt is not the paper. Do not state effect sizes, sample sizes or conclusions that are not in the returned text.
5. If the pastor wants to keep one, find the sermon and call `add_note` with the study as a research note and its DOI. Report what was saved.

## Decision points

- **The claim is stronger than the evidence.** If the pastor's sentence says more than the excerpt shows, say so and suggest wording the excerpt can bear, or suggest reading the paper.
- **Nothing relevant comes back.** Try once with broader or more standard terms. If there is still nothing, say no study was found on that theme. Do not supply a study from memory.
- **A sensitive theme.** For themes such as grief, addiction, abuse, suicide or mental illness, present findings plainly and without advice. If the pastor is asking because someone is in danger now, point to emergency services first: in the United States, 911 for immediate danger and call or text 988 for crisis support.
- **Research and Scripture together.** Keep them in separate parts of the answer. A study does not prove a verse, and a verse does not validate a study.

## Errors and empty results

- A sign in message: ask the pastor to connect and sign in to Sermon Prep.
- A DOI that will not save: report the message as returned and keep the citation in the chat so it is not lost.

## What the answer looks like

Put the studies under the heading the service itself uses: "Outside research, not Scripture". For each study:

```
<Authors> (<year>). <Title>. <Journal>. DOI: <doi>
Excerpt: "<abstract excerpt as returned>"
What it supports: <one cautious sentence>
```

Then one line on limits: the excerpt is partial, the paper should be read before it is quoted from the pulpit, and the paper belongs to its publisher and authors.

## Examples

**"Find research on gratitude and wellbeing for Sunday."**
Call `find_research` with a theme such as "gratitude wellbeing". Show the two or three most relevant results, reviews first, each with authors, year, journal, DOI and excerpt, under the heading "Outside research, not Scripture". Offer to save one to the sermon.

**"I want to say that most lonely people are elderly. Is that right?"**
Call `find_research` on loneliness and age. Report what the returned excerpts say. If none supports the sentence as worded, say so, and do not fill the gap with figures from memory.

**"Save the second one to my Philippians sermon."**
Call `list_sermons` to find the sermon, then `add_note` with that study as a research note and its DOI. Confirm the sermon and the study saved.
