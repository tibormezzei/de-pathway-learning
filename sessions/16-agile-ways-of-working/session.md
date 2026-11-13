# Session 16: Ways of working: Agile in data teams

| | |
|---|---|
| Module | 4: Delivering and working with people |
| Wiki skill(s) | Problem resolution (data): Agile and roles, Jira; Problem resolution: documentation, pair programming |
| HEO target level | Awareness (the wiki's HEO target), working towards Working |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session) |
| Prerequisites | Session 15 (the school attendance brief and design docs) |
| Dataset | None. The exercise uses session 15's brief |

## Learning outcomes
By the end of the session, participants can:
1. Compare Agile and waterfall, and explain why Agile suits uncertain data work.
2. Describe Scrum (roles, events, artefacts) and Kanban, and the team's place in them.
3. Write user stories for data work as **vertical slices**, with testable **acceptance criteria**.
4. Size and order a backlog, and explain MVP, spikes and the definition of done.
5. Use Jira effectively, and know the ONS roles that sit alongside Agile roles (IAO, DisCO).

## Concept outline
| Min | Section |
|---|---|
| 0–3 | Peer swap of session 15 design docs, using the rubric (optional) |
| 3–8 | Waterfall vs Agile: why data work is uncertain |
| 8–15 | Scrum: roles, events, artefacts; Kanban |
| 15–22 | User stories for data: vertical slices, INVEST |
| 22–26 | Acceptance criteria: Given / When / Then → tests |
| 26–29 | Estimation, spikes, MVP, definition of done |
| 29–32 | Jira in practice; ONS roles alongside Agile |
| 32–35 | CDP today → GCP tomorrow |
| 35–55 | Exercise |
| 55–60 | Compare backlogs: who sliced vertically? |

## Exercise
- **Task:** split the school attendance request into vertical-slice stories, write acceptance criteria, size, order and plan sprint 1.
- **Starting files:** `exercise/README.md`, `exercise/story_template.md`, `exercise/definition_of_done.md`
- **Done when:** a backlog of stories (no L sizes), Given/When/Then for the top 3, a sprint 1 plan and an agreed definition of done.
- **Reference:** `solutions/example_backlog.md`

## Further learning (from the wiki)
- [Atlassian: Jira getting-started guide](https://www.atlassian.com/software/jira/guides/getting-started/introduction#what-is-jira-software)
- [Learning Hub: Project delivery learning suite](https://learninghub.ons.gov.uk/course/view.php?id=682) · [Agile Percipio channel](https://ons.percipio.com/channels/e4be53b0-f9ee-11e6-9896-0776e4b35762?tab=WATCH)
- [Learning Hub: DisCO training](https://learninghub.ons.gov.uk/course/view.php?id=659)
- Pair programming: [Datadog](https://www.datadoghq.com/knowledge-center/pair-programming/), [Codecademy](https://www.codecademy.com/resources/blog/what-is-pair-programming/)
- For later (practitioner/expert): [Ultimate Agile e-learning](https://www.thescrummaster.co.uk/courses/ultimate-agile-elearning-course/), [Ultimate Scrum course](https://www.thescrummaster.co.uk/courses/ultimate-scrum-course/)

## Facilitator notes
- Ask a delivery manager or product owner to play the product owner in the exercise. They answer questions in role ("Do you need phase in the MVP?").
- Most groups start with horizontal stories (ingest, validate, aggregate). Interrupt at 5 minutes and ask "what could the analyst look at after story 1?"
- Make the link explicit: acceptance criteria → pytest tests (slide 9). It ties the module back to sessions 06–07.
