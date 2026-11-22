# Outside research on the Sermon Prep desk

Facts in this file come from the published guide, privacy policy and terms of the Sermon Prep server at https://sermon-prep.mcp.opzero.sh/?page=docs. The `find_research` tool requires sign in, so follow its own schema for argument names and treat the returned fields as the record of what is available.

## Where the records come from

- Research records come from OpenAlex, an open index of scholarly works. The service states the records are CC0.
- A result is a citation with a short abstract excerpt and a link to the paper. It is not the paper.
- The papers themselves belong to their publishers and authors. The service's terms say to follow each paper's own license when quoting it.

## What the service states about results

- Results are peer reviewed studies on the theme, with review articles first.
- Every study shows its authors, year, journal and DOI under the label "Outside research, not Scripture".
- Retracted papers are dropped.
- A study does not prove a verse, and the service gives no clinical advice.
- Outside research shown by the service is not medical, psychological or legal advice.

## What leaves the desk when research is used

From the privacy policy:

- OpenAlex receives the research theme that is typed. It does not receive the pastor's name, account or sermon.
- The DOI registry at doi.org receives the DOI of a study that is saved.
- The service says it does not save or log the themes searched.
- When a study is added to a sermon, the service adds one to a shared count for that study's DOI. The policy describes the count as a number with no text, sermon or name attached.

Because the theme goes to an outside index, phrase it in general terms. Never put a congregant's name or circumstances in a search theme.

## Reading a result honestly

- **An excerpt is partial.** State only what the returned text says. Sample, method, size of effect and limits are usually not in an excerpt. If they matter, the paper has to be read.
- **Reviews first is an ordering, not a verdict.** A review summarizes a field as its authors saw it. A single study reports one result.
- **Association is not cause.** Use the study's own verbs. If the excerpt says "associated with", do not write "causes".
- **Populations differ.** A finding about one group, country or age range may not carry over to a congregation.
- **Date matters.** Give the year. Older findings may have been revised.
- **Peer review is a filter, not a guarantee.** It does not make a finding settled.

## Citing a study in a sermon or handout

Give enough for a listener to find it:

```
<First author> and colleagues, <year>, <journal>. DOI: <doi>
```

Keep the DOI with the citation through `add_note` and `export_sermon`, so the handout carries it. The service's terms say the pastor is responsible for checking any study against its source before use.

## Sensitive themes and people in need

The service is a study aid and not a counseling or crisis service. Research on grief, trauma, addiction, abuse, self harm or mental illness may be useful in a sermon, and it is not guidance for any one person's care. If a request is really about someone at risk, say that this tool cannot advise on care, and point to help: in the United States, 911 for immediate danger and call or text 988 for crisis support. Elsewhere, local emergency services. For ongoing needs, encourage contact with a qualified professional.
