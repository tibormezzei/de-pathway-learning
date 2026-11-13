# Reference answers: session 10

Numbers come from `data/make_data.py` (seed 10).

## Profiling findings

| Column | Finding | Evidence | Impact | Action |
|---|---|---|---|---|
| establishment_id | **Not unique** | 12 IDs appear twice. The second copy has " Ltd" added to the name | Double-counting in totals by authority | Ask the supplier which is current. Dedupe once a rule is agreed |
| business_name | Not unique, even ignoring the duplicates (e.g. 18 × "Golden Diner") | value counts | Can't be used as a key | Ignore as a key |
| business_type | Clean, 7 categories | value counts | None | None |
| address_postcode | 4 shapes; **129 (~1 in 10)** compact or lower case; **44 blank** | `patterns()`: `aa999aa`, `aa99aa` | Matching to geography or other data will fail without standardising | Fix in pipeline (normalise, session 06!). Count and report the blanks |
| local_authority | **8 spellings for 5 authorities** (Newport ×3, BANES ×2) | value counts | Totals by authority would be split and wrong, which is **the core of the publication** | Fix in pipeline with an agreed lookup. Ask the supplier to standardise at source |
| rating_value | **Mixed**: numbers 0–5 plus `Exempt` (78) and `AwaitingInspection` (63) | `numeric_%` ≈ 88% | Can't average it naively. Text values must be handled explicitly | Keep as a category. Agree how Exempt and Awaiting are presented |
| rating_date | **66 × `1900-01-01`** (sentinel) and 75 blank, both for uninspected premises; **3 in 2031** (future) | top values, max | Sentinels distort "date of last inspection" stats. Future dates are impossible | Treat the sentinel as missing. Ask the supplier about the future dates |
| scores | Blank exactly where the rating is Exempt or Awaiting | cross-tab | As expected, but check it stays that way | Validate the relationship (session 08) |
| scheme_type | **Constant**: `FHRS` for all 1,212 rows | `distinct` = 1 | No information | Drop, or keep as a check |
| fax_number | **~99% blank** | `blank_%` | No use | Drop (and it's contact data we don't need: data minimisation) |
| latitude / longitude | ~8% blank; **6 rows at 0,0** ("null island", off the coast of Africa) | top values, min | Maps or geography would show points in the Atlantic | Treat 0,0 as missing. Ask about geocoding |

## Source system analysis
- **Grain and key:** one row per establishment, current rating only. The key is `establishment_id`, but it **isn't reliable** (duplicates).
- **Update pattern:** weekly full extract. The pipeline can **replace** rather than merge each week, but it should **keep each week's extract** if trends over time are ever needed.
- **History:** previous ratings and appeal outcomes aren't included. Any "change since last year" statistics are impossible unless we store the weekly snapshots ourselves.
- **Ownership:** five authorities enter data into one system. Data quality problems may be **authority-specific**, so look at quality by authority.

## Good supplier questions
1. 12 establishment IDs appear twice with slightly different names. Which row is current, and why does this happen?
2. Can local authority names be sent as a code (e.g. ONS GSS code) rather than free text?
3. What do `1900-01-01` and blank rating dates each mean? Are they different?
4. Three ratings are dated 2031. Are these keying errors, and what should they be?
5. If a rating changes on appeal, does the extract show the new rating, the original one, or both?

## What a good stakeholder write-up looks like (example)
> **Can we publish ratings by local authority? Yes, after two fixes.**
>
> 1. **Authority names are recorded inconsistently.** Newport appears three different ways and Bath & NE Somerset two ways. If we published as-is, Newport's figures would be split into three rows. *We can fix this in our processing, and we'll ask the supplier to standardise it.*
> 2. **A small number of businesses appear twice** (12 out of about 1,200). Left alone, this slightly overstates some counts. *We need the supplier to tell us which record is correct.*
> 3. **The extract only shows each business's current rating.** We can publish today's picture, but not changes over time, unless we start keeping a copy every week. *We recommend starting that now.*
>
> Smaller issues (missing postcodes and map locations for about 1 in 12 businesses) don't affect a table by authority, but would matter for a map.

Teaching point: the write-up leads with **the decision**, explains **impact rather than technique**, and separates **what we can fix** from **what we need from others**.
