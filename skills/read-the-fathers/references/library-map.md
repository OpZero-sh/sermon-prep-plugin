# Church Fathers Library: volumes, section ids and citation

The volume list, id formats and behavior described here come from the Church Fathers Library server: its `list_volumes`, `volume_contents`, `find_sections` and `read_section` results and its public guide at https://church-fathers-library.mcp.opzero.sh/?page=docs. The section headed "Bibliographic notes from outside the tool" is general knowledge about the edition and is marked as such.

## The collection

- 38 volumes: the Ante-Nicene Fathers (10), the Nicene and Post-Nicene Fathers, Series 1 (14) and Series 2 (14).
- English translations made in the 1880s. No Greek, Latin or Syriac text.
- The texts come from the Christian Classics Ethereal Library, which marks them public domain. The server keeps a cached copy and states that requests are not stored.

## Volume ids and contents

The list below is the server's own summary of each volume. Call `list_volumes` for the current list.

### Ante-Nicene Fathers: `anf01` to `anf10`

| Id | Covers |
| --- | --- |
| `anf01` | Clement of Rome, Mathetes (Diognetus), Polycarp, Ignatius, Barnabas, Papias, Justin Martyr, Irenaeus |
| `anf02` | Hermas, Tatian, Athenagoras, Theophilus, Clement of Alexandria |
| `anf03` | Tertullian |
| `anf04` | Tertullian, Minucius Felix, Commodian, Origen |
| `anf05` | Hippolytus, Cyprian, Caius, Novatian |
| `anf06` | Gregory Thaumaturgus, Dionysius the Great, Julius Africanus, Anatolius, Methodius, Arnobius |
| `anf07` | Lactantius, Venantius, Asterius, Victorinus, Didache, Apostolic Constitutions, early liturgies |
| `anf08` | Testaments of the Twelve Patriarchs, Clementine literature, apocrypha, Edessa and Syriac documents |
| `anf09` | Gospel of Peter, Diatessaron of Tatian, Apocalypse of Peter, Origen on John and Matthew |
| `anf10` | Bibliographic synopsis and general index |

### Nicene and Post-Nicene Fathers, Series 1: `npnf101` to `npnf114`

| Id | Covers |
| --- | --- |
| `npnf101` | Augustine: Confessions, Letters |
| `npnf102` | Augustine: City of God, Christian Doctrine |
| `npnf103` | Augustine: On the Trinity, doctrinal and moral treatises |
| `npnf104` | Augustine: against the Manichaeans and Donatists |
| `npnf105` | Augustine: anti Pelagian writings |
| `npnf106` | Augustine: Sermon on the Mount, Harmony of the Gospels, homilies on the Gospels |
| `npnf107` | Augustine: homilies on John and First John, Soliloquies |
| `npnf108` | Augustine: Expositions on the Psalms |
| `npnf109` | John Chrysostom: On the Priesthood, ascetic treatises, homilies on the Statues |
| `npnf110` | John Chrysostom: homilies on Matthew |
| `npnf111` | John Chrysostom: homilies on Acts and Romans |
| `npnf112` | John Chrysostom: homilies on First and Second Corinthians |
| `npnf113` | John Chrysostom: homilies on Galatians through Philemon |
| `npnf114` | John Chrysostom: homilies on John and Hebrews |

### Nicene and Post-Nicene Fathers, Series 2: `npnf201` to `npnf214`

| Id | Covers |
| --- | --- |
| `npnf201` | Eusebius: Church History, Life of Constantine |
| `npnf202` | Socrates and Sozomen: church histories |
| `npnf203` | Theodoret, Jerome, Gennadius, Rufinus: historical writings |
| `npnf204` | Athanasius: select works and letters |
| `npnf205` | Gregory of Nyssa: dogmatic treatises |
| `npnf206` | Jerome: letters and select works |
| `npnf207` | Cyril of Jerusalem, Gregory Nazianzen |
| `npnf208` | Basil the Great: letters and select works |
| `npnf209` | Hilary of Poitiers, John of Damascus |
| `npnf210` | Ambrose: select works and letters |
| `npnf211` | Sulpitius Severus, Vincent of Lerins, John Cassian |
| `npnf212` | Leo the Great, Gregory the Great |
| `npnf213` | Gregory the Great, Ephraim the Syrian, Aphrahat |
| `npnf214` | The Seven Ecumenical Councils |

### Finding a preacher on a book of the Bible

For a sermon text, the homily and commentary series are usually the fastest route to sustained comment.

| Bible book | Where to look |
| --- | --- |
| Psalms | Augustine, `npnf108` |
| Matthew | Chrysostom, `npnf110`. Augustine on the Sermon on the Mount, `npnf106`. Origen, `anf09`. |
| John | Augustine, `npnf107`. Chrysostom, `npnf114`. Origen, `anf09`. |
| Acts, Romans | Chrysostom, `npnf111` |
| 1 and 2 Corinthians | Chrysostom, `npnf112` |
| Galatians through Philemon | Chrysostom, `npnf113` |
| Hebrews | Chrysostom, `npnf114` |
| 1 John | Augustine, `npnf107` |

## Section ids

- A section id is a dotted path of Roman numerals, such as `viii`, `viii.iii` or `viii.iii.ix`. Some levels use capitals, as in `vi.VIII` for Book VIII of the Confessions. Copy ids exactly as a tool returns them.
- `volume_contents` lists a volume's headings to a chosen depth of 1 to 3 and pages with `offset`. Depth 1 shows the works and front matter. Deeper levels show books and chapters.
- `find_sections` matches words in section titles across all 38 volumes, or in one volume when `volume` is given. It does not search the body text. A scripture reference or a topic is not a title and usually returns nothing.
- Titles are the edition's. The Didache is The Teaching of the Twelve Apostles in `anf07`. A similar title, The Teaching of the Apostles, in `anf08` is a different document. Chapter and book numbers in titles are Roman numerals.

## What `read_section` returns

1. The section title, then the volume title and the section id.
2. The text. Long sections come in pages of about 6000 characters.
3. With `notes: true`, a numbered list of the translators' and editors' footnotes after the text. The notes hold scripture references, cross references to other works and textual remarks. Markers are not shown inside the text, so match a note to its place by content.
4. A last line with the page count and the ids of the next and previous sections.

A section at the top of a work may hold only the title. Follow the next section link to reach the text.

## Works printed in more than one version

For the letters of Ignatius the edition prints the shorter and the longer version in the same section. In the returned text each passage appears twice in succession, shorter version first and longer version second, with no label between them. A Syriac version is printed in separate sections, for example for the letter to the Romans.

When quoting Ignatius, say which version the words come from. If the two paragraphs are hard to tell apart, the longer one is the one with added phrases.

## Citation template

```
<Author>, <Work> <book>.<chapter> (<series and volume>, section <id>), English translation of the 1880s.
```

Examples built from live results:

- Didache 9 (ANF 7, The Teaching of the Twelve Apostles, section viii.iii.ix)
- Ignatius, To the Romans, salutation, shorter version (ANF 1, section v.v)
- Augustine, Confessions, Book VIII (NPNF Series 1, volume 1, section vi.VIII)

Give the section id so that anyone with the connector can reopen the passage. In a printed handout the series, volume and the work's own book and chapter numbers are enough.

## Limits the service states

- Searches match section and chapter titles, not every word of the text.
- Long sections come in pages of about 6000 characters.
- English translations only, from the 1880s.

## Bibliographic notes from outside the tool

These points are not returned by the server. They are standard facts about the edition, included because citations and attributions are easy to get wrong.

- The server and the Christian Classics Ethereal Library label the whole set the Schaff edition. In a formal citation, the Ante-Nicene Fathers were edited by Alexander Roberts and James Donaldson, with the American edition revised by A. Cleveland Coxe. The Nicene and Post-Nicene Fathers were edited by Philip Schaff for the first series and by Schaff and Henry Wace for the second.
- Scholarship has moved since the 1880s. Some works in these volumes are now dated or attributed differently, and for some a better text has since been established. Of the two Greek versions of Ignatius printed together, the shorter is the one generally accepted as his, and the longer is generally regarded as a later expansion. When a sermon leans on who wrote a text or when, advise checking a current reference work.
- The Fathers quote Scripture from Greek and Latin Bibles. Their wording, and for the Psalms their numbering, can differ from a modern English Bible.
