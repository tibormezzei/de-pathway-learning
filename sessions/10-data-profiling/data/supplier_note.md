# Supplier note: food hygiene inspections extract (fictional)

> Sent by the regulatory services data team with the first extract.

Hi,

Attached is `inspections.csv`, one row per establishment, taken from our inspection management system. Some notes:

- It's a **full extract**. We can send it **weekly**, usually on Monday mornings.
- Each row shows the establishment's **current** rating. We don't keep previous ratings in this extract.
- Businesses can **appeal** a rating, and the rating can change after the appeal.
- Five local authorities share the system, and each one enters its own data.
- Coordinates are added by a separate geocoding process, which doesn't always find a match.
- New establishments are rated "AwaitingInspection" until their first visit. Some low-risk premises are "Exempt".
- Our schema documentation is a bit out of date, so let us know if anything is unclear.

Thanks,
Regulatory Services Data Team
