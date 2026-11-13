# Scenario: the survey field operation (fictional)

> Notes from a requirements conversation with the field operations manager.

"We run several household **surveys**, the Labour Force Survey and the Living Costs and Food Survey for example. Each survey has a code and a name.

Every month (we call it a **period**) we take a sample of **addresses** for each survey. An address that's been issued to a survey for a period is what we call a **case**. The same address can be sampled for different surveys, and occasionally for the same survey again in a later period.

Each case is allocated to one **interviewer**. Interviewers work in one **region**, and addresses are in a region too. Normally an interviewer only gets cases in their own region, but when we're short-staffed someone may cover a neighbouring region.

Interviewers make **visits** to the address, as many as it takes up to a limit. Every visit is recorded with a date and an **outcome**, such as 'no contact', 'refusal' or 'full interview'. Outcomes come from a standard list of codes. The outcome of the **last** visit is the case's final outcome.

At the moment it's all kept in one big spreadsheet export, one row per visit (`data/case_visits_flat.csv`). It's a nightmare. When an interviewer's name changes we have to edit hundreds of rows, and we've got outcome descriptions spelt differently in different places."
