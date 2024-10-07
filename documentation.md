---
title: Technical Introduction
subtitle: For the Provisional Transcription of the *Piers Plowman* Text in Takamiya MS 23
author: Ian Cornelius
date: October 7 2024
---

\newfontfamily\myfont{GFS Porson}
\newcommand{\myalpha}{\begingroup\myfontα \endgroup}
\newcommand{\mybeta}{\begingroup\myfontβ \endgroup}
\newpage

# Summary overview

The XML file `transcription-takamiya-23.xml` contains a provisional transcription of the text of *Piers Plowman* as transmitted in New Haven, Beinecke Library, Takamiya MS 23 (*olim* London, Sion College, MS Arc. L.40. 2/E), designated sigil 'S' in the textual scholarship.
For description of the manuscript and its text, see @CorneliusTakamiyaMS232023, with references.
This document serves as a technical introduction to the transcription file and policies that inform it.

The transcription agrees approximately with *TEI P5 Guidelines for Electronic Text Encoding and Interchange* and the conventions of published documentary editions of *The Piers Plowman Electronic Archive* (*PPEA*).
See @TEIConsortiumTEIP5Guidelines2024 and @DugganPiersPlowmanElectronic2014a].
These authorities differ in detail; the present documentation does not attempt to reconcile them.
Readers are referred to *TEI P5 Guidelines* for additional commentary on individual elements.

The transcription differs from published *PPEA* editions in presenting a bare diplomatic transcription, without a textual apparatus or editorial notes of any kind.
It also differs from published editions in not being peer reviewed.
For bibliographical and licensing details, see [Licensing and Citation].

# Document history and responsibility

The initial transcription was produced by Matt Davis, J. Eric Ensley, Jim Knowles, and Timothy L. Stinson in 2014, based on archival-grade TIFF scans of the manuscript, captured in the Beinecke Library's digitization lab in that year.
In 2017 responsibility for the transcription passed to Ensley and Ian Cornelius as co-editors, assisted by Paul A. Broyles as technical co-editor.
Additional contributions were made by Jesse McDowell and Chelsea Skalak.
Cornelius is responsible for documentation.

As co-editors Cornelius and Ensley have checked the transcription in full against the TIFF scans, spot-checked against the manuscript in cases of doubt, and aligned the transcription with articulated policy.

# Document structure

The `body` element of the transcription file supplies a complete transcription of the *Piers Plowman* text.
Divisions of the text into *passus* are recorded within `div1` elements.
For instance, the text of the Prologue is wrapped within the tags

``` {.xml}
<div1 type="passus" n="S.P" org="uniform" sample="complete">
...
</div1>
```

The `sample` attribute records that the transcription is complete, that is, comprises the entire text transmitted in the manuscript.
This value makes no claim about the completeness of the manuscript.

Divisions of leaf and side are recorded by the element `milestone`,[^milestone] for instance:

``` {.xml}
<milestone unit="fol." n="1r"/>
```

[^milestone]: The element `milestone` also redundantly records divisions of *passus*, in agreement with current practices of *PPEA*.
See for instance the XML source of @JeffersonPiersPlowmanElectronic2014.

Bibliographical signatures, entered by the scribe to record the sequence of gatherings and leaves, are recorded within `fw` elements, for instance:

``` {.xml}
<fw type="sig" place="bottomRight">A2</fw>
```

Discourse lines (each usually construable as one complete metrical line of alliterative verse) are recorded within `l` elements and have the attributes `xml:id`, `n`, and `n_Bx`.
These attributes have the following semantics:

- `xml:id` Consecutive numbering of discourse lines within *passus*, as transmitted by the manuscript.
This attribute supplies a unique identifier for units of transcription.
- `n` Cross-reference to the corresponding line or lines in @KanePiersPlowmanBVersion1988.
- `n_Bx` Cross-reference to the corresponding line or lines in @BurrowPiersPlowmanBversion2018.[^Bx]

[^Bx]: An earlier version of @BurrowPiersPlowmanBversion2018 is available online at <https://piers.chass.ncsu.edu/texts/Bx>.
The attribute `n_Bx` is a customized addition in this transcription of Takamiya 23, unsupported by *PPEA* validation schemas.

Accordingly, the first line of *Piers Plowman* as transmitted by the Takamiya manuscript is encoded as

``` {.xml}
<l xml:id="S.P.1" n="KD.P.73" n_Bx="Bx.P.73">And cam vp kneling / to kisse
  his bulles</l>
```

Subsequent line-number references in this documentation are to the values of the attribute `xml:id` in `l` elements.

Marginalia are recorded within `marginalia` elements.
The attribute `id` anchors each `marginalia` element to the nearest `l` element.
Some `marginalia` elements supply a transcription of the marginal inscription (e.g., S.15.98.m.1); others only flag the existence of a marginal inscription (e.g., S.15.392.m.1).

# Transcription

## Character encoding

The transcription file employs UTF-8 character encoding.
The scribe's Tironian logograph for English *and* and Latin *et* is transcribed by the XML character entity `&amp;`.
The transcription employs these non-ASCII characters:

- Small and capital thorn: *þ* (U+00fe) and *Þ* (U+00de)
- Small and capital yogh: *ȝ* (U+021d) and *Ȝ* (U+021c)
- Small *o* with tilde: *õ* (U+00f5)
- Small *i* with tilde: *ĩ* (U+0129)
- Small Greek alpha and beta: \myalpha (U+03b1) and \mybeta (U+03b2)

The characters *õ* and *ĩ* are employed in transcription of *nomina sacra* only: see [*Nomina sacra*].
The characters \myalpha and \mybeta are employed in cross-references to @KanePiersPlowmanBVersion1988.

The scribe writes an undifferentiated *þ*/*y* graph, transcribed as *þ* or *y*, depending on the phonetic value of the graph and the spelling conventions in Middle English manuscripts that distinguish these letters.[^thorn-y]
The *ȝ*/*z* graph is similarly disambiguated.

[^thorn-y]: This policy is supported by the scribe's care to differentiate forms otherwise homographic.
For instance, though the scribe writes a single form for *þ* and *y*, ÞOU and YOU are precisely distinguished in the writing system: the scribe always writes YOU in full, without abbreviation, whereas ÞOU is written either with initial *th-*, as *thou*, or with the *y/þ* graph and superscripted *u*.


Allographs are not differentiated in the transcription, except that we aim to record majuscules as capitals.
For the letters *B*, *D*, *H*, *K*, *L*, *V*, and *W*, the scribe has a continuum of forms, running between unambiguous minuscule and unambiguous majuscule.
Where these seven letters appear in word-initial position, the choice to transcribe as lower case or capital is often arbitrary.

Large two-lobed "buckled" *a* is transcribed as capital *A* in all instances.[^buckled-a]
Initial double *f* is transcribed as *F*.
Majuscule *I/J* is transcribed as *I*.
We follow the scribe's disposition of *u* and *v*.

[^buckled-a]: For this graph see @PettiEnglishLiteraryHands1977 [plates 13, 17, and 24]; and @DawsonElizabethanHandwriting150016501966 [plates 3 and 7].

## Line division

Where a discourse line runs across two or more text lines, line breaks are recorded with the tag `<lb/>`: for instance, S.1.32.
Overflow onto an adjacent line at the right margin is not tagged.
Instead, we record the punctuation-marks entered by the scribe around the textual overflow, usually a double *virgula*: for instance, S.5.291.

## Punctuation

Marks of punctuation are transcribed with the nearest corresponding ASCII character:

- full stop (`.`) for *punctus*
- slash (`/`) for straight sloping *virgula suspensiva*
- comma (`,`) for smaller semicircular *virgula suspensiva*
- question mark (`?`) for question mark or *punctus percontativus*[^percontativus]

[^percontativus]: The scribe's form opens to the right. See @ParkesPauseEffectIntroduction1993 [53 and plates 34 and 35] and @PettiEnglishLiteraryHands1977 [plates 53 and 54].


Scribal spacing around punctuation-marks is not retained: punctuation-marks within the line are transcribed with a space-character before and after.
Line-ending punctuation-marks are transcribed with a single preceding space-character.

## Tagged features

Text segments with distinctive features are enclosed within tags, as follows:

- `add` encloses text added by the scribe as correction.
  The location of the added text is recorded with the attribute `location`.
  Values are `inline` and `supralinear`.
- `choice` encloses certain scribal abbreviations and their expanded forms, with child elements `abbrev` and `expan`. See [*Nomina sacra*].
- `damage` encloses text affected by post-production damage to the manuscript, usually cropping of leaves.
- `del` encloses text deleted by the scribe.
  Methods of deletion are distinguished with the attribute `rend`.
  Values are `blotted`, `linedThrough`, `overwritten`, and `razedOut`.
- `expan` encloses alphabetic characters supplied in transcription as expansions of scribal abbreviations. See [Abbreviations].
- `foreign` encloses text not in English.
  Language identity is recorded with the attribute `xml:lang`.
  Values are `LAT` (Latin) and `FRE` (French).
- `hi` encloses text with graphic features different from the scribe's usual writing.
  The quality of the difference is recorded with the attribute `rend`.
  Values are `ul` (underlined text), `boxed` (boxed text), `tx` (engrossing script), and `displayScript` (engrossing script).[^tx]
  We assume that the scribe's notional unit of underlining was the word: when, as often, an underline fails to coincide with word boundaries, the partially underlined word is transcribed as underlined in full or not at all, according to our interpretation of the scribe's intentions.
- `sic` encloses uncorrected scribal slips of the pen.
- `unclear` encloses unclear or illegible text.
  Illegible letters are recorded as full stops.

Examples of these tags may be found by searching the XML file.

[^tx]: To the extent that the scribe differentiated two grades of engrossing script, the one designated `tx` in the transcription is used for Latin, while the one designated `displayScript` is used for openings of page and *passus*.
Yet the two grades shade into one another: a saner policy would recognize a single engrossing script, avoiding over-fine distinctions.

## Abbreviations

### General policies on abbreviations

To the extent possible, scribal abbreviations are expanded in accordance with unabbreviated forms elsewhere in the manuscript.
Latin text presents few difficulties, but otiose strokes and spelling variation in the English text generate difficulties typical of medieval and early modern forms of this language [see @ParkesEnglishCursiveBook1969, xxix--xxx].

For lexical items with variable spelling, the majority spelling determines the expansion of abbreviated forms.
For lexical items always abbreviated by the scribe, expansion is guided by the usual value of a given mark of abbreviation in this manuscript and by common spelling conventions of sixteenth-century English.
An example is SERVANT, a word always abbreviated in the scribe's writing but plausibly expanded as

``` {.xml}
s<expan>er</expan>u<expan>au</expan>nt
```


### Treatment of *tittle*

Superscripted bar or *tittle* presents well-known difficulties [@DawsonElizabethanHandwriting150016501966, 19-20; @PettiEnglishLiteraryHands1977, 22].
We treat this mark as an abbreviation only where the resulting expanded form is confirmed in the scribe's unabbreviated spellings.
*Tittles* judged non-abbreviatory are simply ignored in the transcription.
This policy has the following general results:

- *Tittle* is ignored as non-abbreviatory in *man*, *can*, *gan*, *son*, and similar forms, for double -*nn* never appears in word-final position in the scribe's unabbreviated spellings.
- *Tittle* is usually expanded to *n* in the context of *-Vne* and *-Vne-*, where *V* is a vowel other than *u*.
  For instance, *sone* with *tittle* is transcribed as `so<expan>n</expan>ne` and *manes* with *tittle* is transcribed as `ma<expan>n</expan>nes`.
  Spellings with medial double *-nn-* regularly occur in this context.
- *Tittle* is ignored as non-abbreviatory in the context of *-une*, for such words are never spelled with double *n*.
  For instance, DOWN is always spelled *doune*, whether *tittle* is present or not.
- Expansion contexts for *m* differ from those to *n*.
  For instance, *some* with *tittle* is not expanded to *somme*, as the unabbreviated spelling *somme* does not occur.

These patterns of scribal spelling are obviously motivated to avoid minim confusion.
That is, the scribe's unabbreviated spellings are themselves constrained, and this observation exposes a logical fault in the treatment of unabbreviated spellings as a neutral 'decoding key' for marks of abbreviation.

An alternative approach would transcribe *tittle* with a special glyph, as a functional component of the scribe's writing system, in certain cases possibly irreducible to any alphabetic character string.
Support for such an approach comes from lexical items in which *tittle* may serve to disambiguate forms otherwise homographic.
An example is supplied by the array of spellings for SOON, SON, and SUN (*tittle* is recorded by a trailing tilde [`~`]):

- SOON: *sone* (21x)
- SON: *son\~* (28x), *sone\~* (5x), *son* (1x), *sonne* (1x), *sonne\~* (1x)
- SUN: *sonne\~* (12x), *sonne* (8x)

In the five instances of *sone\~* SON, *tittle* has diacritic function, distinguishing the base spelling *sone* from both *sone* SOON and *sonne* SUN: that is, the form *sone\~* is unambiguous only so long as *tittle* is neither ignored nor expanded.
On this evidence, *tittle* is a functional component of the scribe's orthography, but not a central component.[^poor]

[^poor]: The array of spellings for POOR and POWER supplies another example of a mark of abbreviation serving to distinguish lexical items otherwise homographic.
The scribe writes POOR as *poore* (12x), *pore* (6x), *poor* (1x), or *pou'* with *-er/-re* abbreviation (64x), whereas POWER is written as *poure*, always without abbreviation (23x).
The sole exceptions to this pattern are S.13.257 and S.14.236, where POWER is written with the *-er/-re* abbreviation;
and S.15.338, where POOR is written as *poure*, without abbreviation.
The usual form of each word is illustrated in S.3.169: `pou<expan>re</expan> men maie haue no poure`.


### *Nomina sacra*

Uniquely in transcription of *nomina sacra*, we employ a markup syntax that permits representation of both the scribe's brevigraph and a transliterated expansion.
This is done with the element `choice` and its child elements `abbrev` and `expan`, for instance:

``` {.xml}
<choice><abbr>xpĩ</abbr><expan>cristi</expan></choice>
```

Brevigraphs are transcribed in Roman letters and expanded in agreement with unabbreviated spellings elsewhere in the manuscript.
The transcription employs the following value-pairs for `abbrev` and `expan`:

- `Ihu` : `Iesu`
- `Ihus` : `Iesus`
- `xp` : `crist`
- `xi` : `cristi`
- `xpĩ` : `cristi`
- `xpm` : `cristum`
- `xpõ` : `cristo`
- `xps` : `cristus`

## Word division

### Words divided by the scribe

Contiguous morphs treated by the *Oxford English Dictionary* (*OED*) as constituents of a single word, but written with separating spaces by the scribe, are joined by a shadow hyphen in the transcription.
For instance:

``` {.xml}
them<seg type="shadowHyphen">-</seg>self
```

### Words joined by the scribe

Morphs treated by the *OED* as separate words, but run together by the scribe, are run together in the transcription, preserving scribal word-division.
As this policy leaves affected forms unmarked in the transcription, their existence is recorded in this documentation, as follows.

- __Negation of a noun or adjective phrase with *no*__.
The negative particle *no* may be run together with the following word:
*noking* (1x),
*nolesse* (1x),
*noman* (31x),
*nomo* (1x),
*nomore* (13x),
*nowise* (2x).
In each case the following word is monosyllabic and the combined form is construable as a single accentual group.

- __Negation of a verb phrase with *not*__.
The negative adverb *not* may be run together with a preceding verb.
Most instances involve an auxiliary or form of *be*:
*benot* (1x),
*couldnot* (1x),
*darenot* (2x),
*hadnot* (1x),
*maynot* (17x),
*shallnot* (2x), *shalnot* (1x),
*shaltnot* (1x),
*willnot* (7x), *wilnot* (7x),
*woldnot* (1x).
More rarely, a lexical verb is involved:
*carenot* (1x),
*lokenot* (1x),
*workethnot* (1x),
*wotnot* (2x).
The form *workethnot* is the only item involving a disyllable.

- __Auxiliaries followed by *be*__.
*Shall* and *will* are run together with following *be* or *become*:
*shalbe* (31x),
*wilbe* (10x),
*wilbecome* (1x).
These combined forms have reduction of double *-ll*, seen also in *shalnot*, *wilnot*, *alabout*, and *welnere*.
The two-word form *shall be* does not occur.

- __Phrasal verbs__.
A phrasal verb may be run together with the following adverb:
*drawnfourth* (1x),
*rapdoune* (1x).

- __Pronominal subjects__.
A pronominal subject may be run together with in following verb:
*theygo* (1x),
*theybeleue* (1x).

- __Adjectives and quantifiers__.
An adjective or quantifier may be run together with the head noun:
*anyman* (3x),
*allmankynde* (1x),
*euilspeche* (1x),
*lefthande* (2x),
*lyfeholymen* (1x),
*poremen* (1x),
*poureman*/*-men* (3x.).

- __Prepositions__.
Prepositions may be run together with the following element:
*atones* (4x),
*forthat* (2x),
*ina* (1x),
*incase* (5x),
*infeith* (1x),
*onhighe* (2x).
Several of these could be classified instead a compound adverbs.
*Forthat* functions as a compound conjunction.

- __Adverbs__.
A monosyllabic adverb may be run together with the following element:
*alaboute* (1x),
*asmuch* (3x),
*aswell* (2x),
*howlong* (2x),
*howoft* (1x).
*somuche* (6x),
*therbe* (2x),
*thusmuche* (1x),
*welnere* (1x).
The instances with *how* are conjunctive, introducing an indirect question.

### Ambiguous cases

Where the scribe's spacing is inconclusive, permitting interpretation with or without word division, the transcription errs on the side of modern usage, as defined by the *OED*.
Forms affected by this treatment are:

>
*a while* (S.18.168),
*hellewarde* (S.18.117),
*forfare* (S.15.139),
*forsworne* (S.19.375),
*godhede* (S.9.47),
*palfreyes mete* (S.19.421),
*sometyme* (S.16.46, S.16.47),
*tomorowe* (S.2.45),
*westmynstre* (S.20.282),
*without* (S.5.633)

## Elision and contraction

Scribal elisions and contractions are preserved.
For instance: *thaungell* and *tamende*.

# Licensing and citation

This documentation and the XML file `transcription-takamiya-23.xml` are released under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

An adequate citation is:

> Cornelius, Ian, J. Eric Ensley, and Paul A. Broyles, eds. 2024. *New Haven, Beinecke Library, Takamiya MS 23: A Provisional Machine-Readable Transcription of the "Piers Plowman" Text*. Version 0 [2024-10-07]. <https://github.com/icornelius/s-takamiya-23/>.

# Bibliography
