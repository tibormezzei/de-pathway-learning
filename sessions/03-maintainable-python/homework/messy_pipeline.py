# survey pipeline - DO NOT TOUCH works fine
# last edited by ??? ran it on my machine
import pandas as pd
import os
import datetime
import numpy as np

pd.set_option("display.max_columns", 50)

df = pd.read_csv("../data/survey_responses.csv", dtype=str)
print(df.shape)
print(df.head())

# clean region
df["region"] = df["region"].str.strip()
df["region"] = df["region"].str.lower()
for i in range(len(df)):
    r = df.loc[i, "region"]
    if r == "sth":
        df.loc[i, "region"] = "south"
    if r == "wst":
        df.loc[i, "region"] = "west"
df["region"] = df["region"].str.title()
#df = df[df["region"] != "Unknown"]

# dates
d = []
for x in df["interview_date"]:
    try:
        d.append(datetime.datetime.strptime(x, "%Y-%m-%d"))
    except:
        try:
            d.append(datetime.datetime.strptime(x, "%d/%m/%Y"))
        except:
            try:
                d.append(datetime.datetime.strptime(x, "%d-%b-%Y"))
            except:
                d.append(None)
df["interview_date"] = d
print(df["interview_date"].isna().sum())

# age
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df2 = df[df["age"] >= 16]
df2 = df2[df2["age"] <= 120]
print(len(df) - len(df2), "removed")

# dupes
df3 = df2.drop_duplicates(subset=["case_id"], keep="first")
print(len(df2) - len(df3), "dupes")

# month
df3["month"] = df3["interview_date"].apply(lambda x: x.strftime("%Y-%m"))

# work out rates
out = []
for reg in sorted(df3["region"].unique()):
    for m in sorted(df3["month"].unique()):
        tmp = df3[df3["region"] == reg]
        tmp = tmp[tmp["month"] == m]
        issued = len(tmp)
        comp = len(tmp[tmp["outcome"] == "complete"])
        part = len(tmp[tmp["outcome"] == "partial"])
        if issued > 0:
            rr = round((comp + part * 0.5) / issued * 100, 1)
        else:
            rr = 0
        out.append([reg, m, issued, comp, part, rr])

res = pd.DataFrame(out, columns=["region", "month", "issued", "complete", "partial", "response_rate"])
print(res)
if not os.path.exists("../output"):
    os.mkdir("../output")
res.to_csv("../output/response_rates.csv", index=False)
print("done!!")
