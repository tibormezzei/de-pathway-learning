# Brief: weekly school attendance statistics (fictional)

> Email from the Education Analysis team lead.

Hi,

Ministers want **weekly pupil attendance rates**, published every **Thursday at 09:30**, covering the previous school week (Monday–Friday). The breakdowns are:
- by **local authority** (22 of them)
- by **school phase** (primary, secondary, special)
- nationally

**Data we get:**
1. **Daily attendance returns** from each local authority. They arrive as CSV files on an SFTP drop, one file per authority per day, with one row per school: `school_id, date, sessions_possible, sessions_attended, sessions_authorised_absence`. Files usually arrive by 07:00 the next day, but **some authorities are often a day late** and **sometimes resend a corrected file** for a day they've already sent.
2. **The school register**, a reference file from the Department: `school_id, school_name, la_code, phase, open_date, close_date`. It's updated about **monthly**. Schools open, close and occasionally **change phase or authority**.

**Other things you should know:**
- Data is **counts of sessions**, not individual pupils, but some **special schools have under 20 pupils**.
- We're on **CDP** at the moment. The whole area moves to **GCP next year**.
- The numbers will be **official statistics**, so they must be reproducible and quality assured.
- If an authority's data is missing, we'd rather publish without it **and say so** than publish late.

Can you design the pipeline? Nothing fancy for now. We need it running in six weeks.

Thanks
