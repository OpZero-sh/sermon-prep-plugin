---
name: plan-sundays
description: "See the coming Sundays with their church year names, seasons, colours and lectionary year, and set them beside what the pastor has already preached. Use when a pastor is planning a preaching calendar or a sermon series, asks what Sunday is coming, or asks which books of the Bible they have and have not preached. Typical requests: 'what are the next six Sundays', 'what Sunday of the church year is the 29th', 'plan my Advent series', 'which books have I not preached from', 'start sermons for the next four Sundays'."
---

# Plan Sundays

Lay out the coming Sundays and the pastor's preaching record so the pastor can plan. The Sermon Prep desk needs sign in.

The calendar gives names, seasons and colours. It does not give appointed readings. The choice of text is the pastor's.

## When to use

- A pastor wants the church year setting of the coming Sundays.
- A pastor wants to see which books they have preached and which they have not.
- A pastor wants to create sermon records for dates they have chosen.

Use `research-a-passage` once a text is chosen, and `work-on-a-manuscript` to write.

## Tools

All are on the Sermon Prep desk.

| Tool | Effect |
| --- | --- |
| `plan_sundays` | Read only. The coming Sundays with church year name, season, colour and lectionary year. The published guide shows a count of 1 to 12. |
| `list_sermons` | Read only. The pastor's sermons, newest first, with which books have been preached and which have not. |
| `start_sermon` | Creates a sermon with title, passage, preaching date and series. |

The desk tools sit behind sign in, so follow the argument names in each tool's schema at call time. How the church year is computed and what it leaves out are in [references/church-year-on-the-desk.md](references/church-year-on-the-desk.md).

## Workflow

1. Call `plan_sundays` for as many Sundays as the pastor is planning, up to the limit. If its schema accepts a start date, pass the pastor's date. Otherwise it lists from today.
2. Present the Sundays as a table: date, name, season, colour, lectionary year. Give the date with its weekday so an error is easy to spot.
3. If the pastor asks about past preaching or a series, call `list_sermons`. Report the books preached and not preached as returned, and any sermons already dated in the planning window.
4. Ask what the pastor wants to do with the dates. Offer suggestions for texts or a series shape only when asked, and mark them as suggestions.
5. When the pastor has chosen, call `start_sermon` once per sermon with the title, passage, preaching date and series they gave. Confirm each record created.

## Decision points

- **Appointed readings.** The data does not include lectionary readings. Do not state a Sunday's readings from memory as if the tool returned them. Ask the pastor to supply the reading from the lectionary their church uses.
- **Local practice.** The calendar follows common Western usage. Churches differ on names, colours, transferred feasts and saints' days. If the pastor's calendar differs, theirs governs.
- **Eastern churches.** The Sunday names and seasons are Western. A pastor in an Orthodox or Eastern Catholic church should plan from their own calendar.
- **Dates beyond the list.** If the pastor asks about a Sunday further out than the list reaches, say how far the list goes.
- **Creating records.** Do not create sermon records for a whole series on your own initiative. Create the ones the pastor names.

## Errors and empty results

- A sign in message: ask the pastor to connect and sign in to Sermon Prep.
- No sermons yet: say the library is empty, so there is no preaching record to compare against.

## What the answer looks like

A short table of Sundays, then, if asked, a short list of books preached and not preached, then a question about what to plan. Add the note that customs vary between churches when a name or colour is likely to differ locally.

## Examples

**"What are the next six Sundays?"**
Call `plan_sundays` for six. Return a table with date, name, season, colour and lectionary year.

**"Plan my Advent series."**
Call `plan_sundays` far enough ahead to cover the four Sundays of Advent and show them. Call `list_sermons` to see what the pastor has preached before. Ask which texts or theme they have in mind. If they ask for ideas, offer a few and label them as suggestions. Create sermon records only for the dates and passages they confirm.

**"Which books have I not preached from?"**
Call `list_sermons` and report the unpreached books as returned. Do not turn the list into a recommendation unless asked.
