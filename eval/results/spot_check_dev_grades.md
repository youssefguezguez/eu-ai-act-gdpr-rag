# Spot-check grades (dev, 10 answers)

Grader: Claude (a second LLM, not a human). Not fully blind: Claude had already seen the
judge's verdicts on the 5 flagged items (q001 q009 q030 q041 q050); the other 5 were graded
before reading the key. Item numbers follow `spot_check_dev.md`.
Faithful is "n/a" when the answer declined (no claims to check).

| # | id | Claude: correct / faithful | Judge: correct / faithful | Agree | Note |
|---|---|---|---|---|---|
| 1 | q035 | yes / yes | yes / yes | ✓ | Quotes Art. 2(10) |
| 2 | q043 | yes / yes | yes / yes | ✓ | 16, Member States down to 13 |
| 3 | q050 | no / n/a | no / yes | ✓ | Wrong decline: Art. 22 not retrieved |
| 4 | q041 | yes / **no** | yes / no | ✓ | "legal claims" is Art. 9(2)(f), not (e) |
| 5 | q030 | no / n/a | no / yes | ✓ | Wrong decline: Art. 99(5) not retrieved |
| 6 | q013 | yes / yes | yes / yes | ✓ | |
| 7 | q001 | **no / no** | no / no | ✓ | Says "permitted"; Art. 5(1)(f) prohibits. Last sentence uncited |
| 8 | q024 | yes / yes | yes / yes | ✓ | |
| 9 | q008 | yes / yes | yes / yes | ✓ | Borderline partial: never states Art. 6(2) outright |
| 10 | q009 | partial / no | partial / no | ✓ | "it performs profiling" is an inference, not in sources |

Agreement: correctness 10/10; faithfulness 8/8 (where applicable).
Caveat: two LLMs agreeing is weaker evidence than a human check, and the sample is small.
