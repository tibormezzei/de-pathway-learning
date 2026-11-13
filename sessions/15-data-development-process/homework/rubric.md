# Design doc rubric

Use this for self-review, peer review in session 16, or facilitator feedback.

| Area | Developing | Good | Strong |
|---|---|---|---|
| **Objective and requirements** | Restates the email | Clear objective; requirements listed | Requirements numbered, typed and traceable; out-of-scope stated |
| **Sources** | Lists files | Grain, owner, delivery and update pattern for each | Plus known issues and specific questions for owners |
| **Data model** | Output columns only | Grain and keys declared | History handled (register changes as versioned reference data, SCD2) with reasons |
| **Data quality** | "Validate the data" | Specific rules; quarantine | Fail / quarantine / warn per rule; reconciliation; completeness by authority |
| **Late and corrected data** | Not mentioned | Late files handled | Idempotent reprocessing of affected days; a cut-off policy; what's published and flagged |
| **Operations** | "Runs weekly" | Schedule, dependencies | Retries for transient failures only, alerting, backfill, run book, owner |
| **Technology and migration** | Tool names | CDP components named | CDP and GCP mapped; decisions taken now to ease migration |
| **Governance** | Not mentioned | Personal data considered | Disclosure control for small schools; IAO; access; retention |
| **Testing** | "Will be tested" | Unit and integration tests mentioned | Test pyramid with synthetic test data; reconciliation as a runtime test |
| **Communication** | Hard to follow | Clear structure | Diagram; plain language; open questions with owners |
