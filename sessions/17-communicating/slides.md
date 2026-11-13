---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 17"
footer: "Communicating across technical and non-technical audiences"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Communicating
## across technical and non-technical audiences

Session 17 · Module 4: Delivering and working with people

---

## Today

1. Why communication is a core DE skill
2. Know your audience
3. Answer first
4. Translating technical ideas
5. Gathering requirements
6. Risks, bad news and PACE
7. Presenting
8. **Exercise:** explain it to someone who doesn't care how it works

---

## A core data engineering skill

Look back at this series. The hardest problems weren't code:
- "Booked or attended?" (13): **a question to ask**
- "Which duplicate is current?" (10): **a question for the supplier**
- "Latest submission wins, even if invalid?" (07): **a business decision**
- "Wrong lookup version: totals balance, areas wrong" (13): **news to deliver**

Engineers who communicate well **build the right thing** and **get trusted** with more.

---

## Know your audience

| Stakeholder | Cares about | Doesn't care about |
|---|---|---|
| Senior leader | Risk, timing, reputation, decisions | How it works |
| Statistician | Method, correctness, ability to check | Which cluster it runs on |
| Data supplier | What exactly you need from them | Your pipeline's architecture |
| DisCO | Small numbers, identification risk | Spark |
| New team member | What to do when it breaks | The design debates |
| Engineer | Design, trade-offs, edge cases | (everything is interesting) |

**Same pipeline, six different explanations.** Start from *their* question.

---

## Answer first

```
            ┌───────────────────────────┐
            │  ANSWER / RECOMMENDATION  │   "Thursday publication is achievable."
            └─────────────┬─────────────┘
         ┌────────────────┼────────────────┐
   ┌─────┴─────┐    ┌─────┴─────┐    ┌─────┴─────┐
   │ Reason 1  │    │ Reason 2  │    │  Risk     │
   └───────────┘    └───────────┘    └───────────┘
        detail and evidence: only if they ask
```

- **BLUF:** Bottom Line Up Front.
- Senior people often decide in the **first 30 seconds**.
- Emails: put the **ask or decision in the subject line** and the first sentence.

---

## Translating technical ideas

❌ "The join fans out because the lookup isn't unique on the key."
✅ "A reference list had one school twice, so its numbers were counted twice. It's fixed, and we've added a check so it can't happen again."

**Techniques**
- Describe the **impact**, not the mechanism.
- Use **one concrete example** ("Newport appears three ways").
- Analogies, used carefully ("like a spreadsheet VLOOKUP that finds two matches").
- **Meaningful numbers:** "1 in 10 postcodes" rather than "10.6% pattern mismatch".
- **Don't dumb down.** Simplify the words, not the truth.

---

## Gathering requirements

| Do | Example |
|---|---|
| Ask **open** questions | "What decision will these figures support?" |
| Ask for **examples** | "Can you show me last month's spreadsheet?" |
| Find the **edges** | "What should happen if a council is a day late?" |
| **Play back** what you heard | "So: weekly, by LA and phase, published Thursday, and missing LAs flagged rather than delayed. Right?" |
| **Write it down** and share | Numbered requirements (session 15) |

People rarely say the important constraints unprompted. **Ask about the awkward cases.**

---

## Risks and bad news

**Early, specific, with a plan.**

> **Subject: Attendance publication. Risk to Thursday, decision needed by Wed 12:00**
>
> Newport's files for Mon–Tue haven't arrived. If they're not here by Wednesday 18:00, I recommend we **publish without Newport and flag it** (as agreed in the requirements). Alternatively, we delay to Friday.
> **Please confirm by Wednesday 12:00.** I've contacted Newport and will update you at 16:00.

- Bad news doesn't improve with age.
- Bring **options and a recommendation**, not just a problem.
- Say what you **don't know**, and when you will.

---

## PACE: graded assertiveness

For raising concerns, especially with someone more senior:

| Level | Sounds like |
|---|---|
| **P**robe | "Can I check how we're handling the April board change?" |
| **A**lert | "I think the March figures may use the wrong board list." |
| **C**hallenge | "I'm concerned we'll publish three practices in the wrong board. Can we hold until it's checked?" |
| **E**mergency | "We need to stop. These figures are wrong and shouldn't be published." |

Start low and escalate if you're not heard. **Psychological safety** means anyone can say "stop".

---

## Presenting: slides, reports, posters

- **One message per slide**, with a headline that *states* it ("Newport is recorded three ways", not "Local authority analysis").
- **Charts:** label directly, start bar charts at zero, one point per chart.
- **Reports:** summary first, then detail. Use ONS **house style** and **plain English**.
- **Posters:** readable from 2 metres, more picture than text.
- **Accessibility:** sufficient contrast, don't rely on colour alone, alt text, meaningful link text, readable fonts.

---

## CDP today → GCP tomorrow

The migration itself is a **communication project**:

| Audience | What they need to hear |
|---|---|
| Senior leaders | Timeline, risk to publications, cost |
| Analysts and users | What changes for *them* (logins, tables, tools), and when |
| Suppliers | Whether delivery changes (SFTP → bucket?) |
| Your team | Skills, training, who does what |

**Carries over unchanged:** everything today.
**Really changes:** many more people will ask "what does GCP mean for me?" Have a one-sentence answer for each audience.

---

## Summary

- Communication is how you **build the right thing** and **earn trust**.
- **Know your audience**, and start from their question.
- **Answer first**, with detail on request.
- **Impact over mechanism**, concrete examples, meaningful numbers.
- Requirements: **open questions, edges, play back, write down**.
- Bad news: **early, specific, with options**. Use **PACE** to raise concerns.

---

## Exercise (25 min, threes)

**Warm-up:** de-jargon five sentences.

**Role-play:** explain the **session 15 pipeline** in **3 minutes** to a stakeholder card:
Deputy Director · Statistician · LA data contact · DisCO · New team member · Migration lead

- Stakeholder: **stay in role**, interrupt, push back.
- Observer: feedback form, **one thing that worked, one to try**.
- Rotate ×3.

**Next session:** data innovation and ethics.
