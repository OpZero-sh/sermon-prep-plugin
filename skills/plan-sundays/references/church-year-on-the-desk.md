# The church year on the Sermon Prep desk

The statements about the desk come from the published guide of the Sermon Prep server at https://sermon-prep.mcp.opzero.sh/?page=docs. The guide says the church year is computed from the Easter rules by the Liturgical Year service, a public server at https://liturgical-year.mcp.opzero.sh/?page=docs. The sample values below were returned by that public service. The `plan_sundays` tool itself requires sign in, so follow its own schema and treat its output as the record.

## What a Sunday entry holds

| Field | Meaning |
| --- | --- |
| Date | The civil date of the Sunday |
| Name | The Sunday's church year name, for example First Sunday of Advent or Christ the King |
| Season | The season, for example Advent, Lent, or the Season after Pentecost (Ordinary Time) |
| Colour | The usual liturgical colour. Some entries give alternatives, such as purple or blue in Advent. |
| Lectionary year | A, B or C in the three year Sunday cycle |

## Facts worth knowing

- The lectionary year changes on the First Sunday of Advent, not on January 1. In live results, Christ the King on November 22, 2026 is in Year A and the First Sunday of Advent on November 29, 2026 is in Year B.
- The year is computed from the published rules for Easter. No third party data is used.
- The Liturgical Year service covers the years 1600 to 2400.

## What is not included

- **Appointed readings.** The service says lectionary readings are not included and that they wait on written permission from the lectionary's publisher. The lectionary year letter tells the pastor which cycle applies. It does not tell anyone the readings.
- **Saints' days and local feasts.** The calendar follows common Western usage. Local calendars, transferred feasts and saints' days vary by church.
- **Eastern calendars.** Sunday names and seasons are Western. The underlying service can give the date of Orthodox Pascha for a year, and nothing else for the Eastern cycle.

## Working with differences between churches

Churches that keep a liturgical year differ in real ways: the names of Sundays after Epiphany and after Pentecost, whether Advent is purple or blue, when a feast is transferred to a Sunday, and which lectionary is in use. Some churches follow no fixed calendar at all. Treat the returned calendar as a common starting point. When the pastor's own calendar says something different, use theirs and do not correct it.

## The preaching record

`list_sermons` returns the pastor's sermons newest first and reports which books of the Bible have been preached and which have not. The record covers only sermons saved in this library, so a pastor who has preached for years and saved a few sermons here will see most books listed as not preached. Say that when presenting the list. The service works with the Protestant canon of 66 books.
