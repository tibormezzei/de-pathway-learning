# Welcome to the Data Engineering Learning Pathway Homepage

Any questions about the pathway can be directed to the Head of Profession for Data Engineering, the Head of the Data Engineering Community of Practice, or the Capability Team in DGO, DALI. 

The purpose of this learning pathway is to be a place to find resources for learning core data engineering skills. These courses are just suggestions, you don’t have to learn things from these resources. If you have alternatives that you would like to share, please add them. The learning pathway is not: 
* Project specific - project specific training should be managed by your team and treated as separate from the learning pathway.
* A brain dump - this is not intended to be a collection of 100 ways of how to learn git (as an example); it's supposed to be a curated list of the most useful and relevant training. 
* Reinventing the wheel - there are pathways and broad learning resources out there already, which cover more than one of the sub-topics we cover here, see for example [DAPCats Wiki](https://gitlab-app-l-01/DAP_CATS/cdp-guidance-wiki/-/wikis/home), [Data Knowledge Hub](https://officenationalstatistics.sharepoint.com/sites/onswiki/SitePages/Data-Knowledge-Hub.aspx), [roadmap.sh](https://roadmap.sh/), [r/dataengineering](https://dataengineering.wiki/Learning+Resources), [Cloud Skills Boost](https://www.cloudskillsboost.google/paths/16), and the [DGO apprentice SharePoint](https://officenationalstatistics.sharepoint.com/sites/DataArchitectureStaCo/SitePages/Apprenticeship.aspx) which all contain lots of useful training links. What it means to be a data engineer in the ONS overlaps with what it means to be a data engineer elsewhere, so we recommend you use these resources. However, in this roadmap, we intend to collect learning resources that support expectations of an _ONS_ data engineer. 

## How to use this roadmap 

### Remember the 70:20:10 split

The 70-20-10 Model for Learning and Development is a commonly used formula to describe the sources of learning in the workplace.

* 70\% of learning should come from on-the-job experience,
* 20\% should come from relationships (e.g. coaching, feedback, performance discussions),
* 10\% should come from formal training (e.g. structured learning, eLearning, classes).

Given this guide, readers can think of this roadmap as providing suggested learning for only 10\% of your *technical* learning. This roadmap only covers the technical skills and does not cover [civil service behaviours](#behaviours). 

### Structure of the pathway

The pathway is structured according to the [GDD role description for a data engineer](https://ddat-capability-framework.service.gov.uk/role/data-engineer) primarily, secondary to that it follows the [ONS Data Engineer Role Profile](https://officenationalstatistics.sharepoint.com/:w:/r/sites/didatehu/DDaTDocs/Role%20Profiles/Current/Data%20Engineer.docx?d=w107fe26276d045abafbe424030c7e708&csf=1&web=1&e=aurLX6), this role profile is currently undergoing restructuring. Firstly, you select a skill, and then you can look through the different levels of the skill. 

The different levels of expertise are:

* 0 = No knowledge/Skills
* 1 = Awareness: You can describe the fundamentals of the skill and demonstrate basic knowledge of some of the skill's tools and techniques.
* 2 = Working: You can apply the skill with some support and adopt the most appropriate tools and techniques.
* 3 = Practitioner: You can apply the skill without support, determine and use the most appropriate tools and techniques, and share knowledge and experience of the skill.
* 4 = Expert: You can lead and guide a team or organisation in the skill's best practices, and teach the skill's advanced tools and techniques.

It is not enough to just do the training courses. To be an expert, for example, you would have to have led a team to complete a project where that skill was used. Working knowledge would require you to have used the skill in a work project. 

Please note: If for example you are looking to upskill to _practitioner_ level in a skill please don't just look at the _practitioner_ section on the appropriate page. You will usually find lots of helpful resources in the general recourses section first.

This learning pathway does not represent the total training offering of DGO. If you think a [level 5 data engineering apprenticeship](https://www.instituteforapprenticeships.org/apprenticeship-standards/st1386-v1-0) or bootcamp might benefit you, or if you are interested in doing some pair programming/ knowledge sharing, please contact Kayla directly. 

There are some [Pluralsight](https://app.pluralsight.com/library/) courses recommended on this roadmap. DGO has a limited number of licences available to colleagues and if you would like one please speak to Diogo. 

### Keeping a CPD log

A requirement for being part of the Government Digital and Data profession is to maintain your Continuous Professional Development (CPD). Keeping a log of this is a great way to ensure you’re fulfilling this. A CPD log can be a great basis for development chats in check-ins and is a great way to track progress towards your [personal development plan](https://learninghub.ons.gov.uk/course/view.php?id=1292). You can find a template [here](https://officenationalstatistics.sharepoint.com/:u:/r/sites/didatehu/SitePages/Government-Digital-and-Data-Continuous-Professional-Development-(CPD).aspx?csf=1&web=1&e=gWfnbP).   

### Platforms

The further you travel on your data journey the more you are likely to specialise on one particular platform/ set of tools. 
However, there are always core concepts to master as well. Whatever cloud platform you are working on, you should always try to follow the [government cloud first policy](https://www.gov.uk/guidance/government-cloud-first-policy), although this is not always possible. 

![Core skills stream going from left to right (awareness to expert) with two branches coming off, one representing GCP and the other CDP](https://github.com/ONSdigital/data_engineer_learning_pathway/blob/main/wiki_images/specialising.jpg)

The Cloud Data Platform (CDP) can be thought of as an 'extra layer' on top of AWS cloud services, where Cloudera handles the pains of managing infrastructure - whereas if we were to use cloud services directly (e.g. directly use AWS), we would have to manage the infrastructure ourselves. There are positives/negatives of directly using cloud services verses using them via a third party like Cloudera, and depends on what the use case is. At the ONS, we don’t currently have access to all Cloudera services. These services will be added gradually over time. Additionally, both Cloudera and GCP have - and will continue to - change, add, and remove services over time. In the spirit of platform agnosticism, we include here a table of cloud components and the names of the most frequently used services on the two main ONS data platforms. This table is far from exhaustive, there are multiple GCP database services for example, but Cloud SQL is likely to be the one ONS colleagues will use for our business needs.

| **Component**         | **CDP Service**                         | **GCP Service**                                                         |
|-----------------------|-----------------------------------------|-------------------------------------------------------------------------|
| Data lake             | AWS S3 Buckets -   accessed from HUE    | Cloud Storage                                                           |
| Data warehouse        | SQL Server and HDFS   with Hive Tables  | BigQuery                                                                |
| Data transfer         | Polybase                                | Cloud Functions to initiate Dataproc                                    |
| Data   transformation | PySpark via Cloudera   Machine Learning | PySpark via Dataproc (Cloudflow if a team created a brand new pipeline) |
| Database              | SQL Server with SSMS                    | SQL Server with Cloud   SQL                                             |
| Version   control     | GitLab                                  | GitHub                                                                  |

You can find platform specific training for GCP on [Cloud Skills Boost](https://www.cloudskillsboost.google/), you can find ONS specific GCP training on confluence e.g. [CATD homepage](https://confluence.ons.gov.uk/display/CATD/) and in the [Framed GCP Training SharePoint](https://officenationalstatistics.sharepoint.com/:f:/r/sites/DataArchitectureStaCo/Capabilities/framed_gcp_learning?csf=1&web=1&e=K58OlU). There is a small amount of free Cloudera training on [their website](https://education.cloudera.com/store?commit=&page=1&st=free&utf8=) with lots of ONS specific CDP training on the [DAPCats wiki](https://gitlab-app-l-01/DAP_CATS/cdp-guidance-wiki/-/wikis/home). 

### Technology 

We appreciate that users of this roadmap may want to upskill in particular technologies rather than skills. Unfortunately, there is no easy way to search the wiki on an on-net machine without cloning the wiki and `ctrl+f` using an IDE. So instead, we recommend where to look for each technology here. 

#### SQL

If you are looking to upskill yourself in SQL, please look in [[Data analysis and synthesis]]. There are also some labs involving SQL on [Cloud Skills Boost](https://www.cloudskillsboost.google/) and [Cloudera Training](https://education.cloudera.com/store?commit=&page=1&st=free&utf8=). 

#### Python

If you are looking to upskill yourself in Python, first please see the guide for getting started with Python on an on-net laptop on the [ASAP wiki](https://gitlab-app-l-01/ASAP/coding-getting-started-guide/-/wikis/home). For an introduction to Python concepts and code please see [freeCodeCamp](https://www.freecodecamp.org/learn/python-v9/), [Scrimba](https://scrimba.com/learn-python-c03) or the [official Python tutorial](https://docs.python.org/3/tutorial/index.html). All three resources cover more of less the same topics at the same depth. Then see [[Data analysis and synthesis]] and [[Programming and build (data engineering)]] for more specific training.

#### PySpark

And for a similar set of resources for PySpark, see first the [DAPCATS wiki](https://gitlab-app-l-01/DAP_CATS/cdp-guidance-wiki/-/wikis/home). The free [coding](https://www.sparkplayground.com/tutorials/pyspark) and [theory](https://www.sparkplayground.com/tutorials/spark-theory) sections of Spark Playground are good for getting up to speed with the basics. Then also see [[Data analysis and synthesis]] and [[Programming and build (data engineering)]] for specific learning.

## Essential Skills

The list of essential skills for any data engineer
* [[Communicating between the technical and non-technical]]
* [[Data analysis and synthesis]]
* [[Data development process]]
* [[Data innovation]]
* [[Data integration design]]
* [[Data modelling]]
* [[Metadata management]]
* [[Problem resolution (data)]] including Agile working
* [[Programming and build (data engineering)]]
* [[Technical understanding]]
* [[Testing]] including test driven development (TDD)

Note that data engineers have four skills in common with data architects and so some resources you find on the communicating, data analysis, data modelling, and metadata management pages have been taken directly from the data architect learning pathway. We thank the DAB team for their help with these sections. 

The data engineer role profile also outlines essential responsibilities for a data engineer at each level. The [role profile]((https://officenationalstatistics.sharepoint.com/:w:/s/didatehu/EUgLlINyWHROgQxfH_C0sQQBYBATTqwXHZEk9qQSej9RMQ?xsdata=MDV8MDJ8TWljaGFlbGEuTGF3cmVuY2VAb25zLmdvdi51a3xiZjE3YWNiNGJmZTE0YjQ1OGY5MTA4ZGQ0YjVlNjIzMHwwNzg4MDdiZmNlODI0Njg4YmNlMDBkODExNjg0ZGM0NnwwfDB8NjM4NzQ5NTkwOTM0OTIzMjA1fFVua25vd258VFdGcGJHWnNiM2Q4ZXlKRmJYQjBlVTFoY0draU9uUnlkV1VzSWxZaU9pSXdMakF1TURBd01DSXNJbEFpT2lKWGFXNHpNaUlzSWtGT0lqb2lUV0ZwYkNJc0lsZFVJam95ZlE9PXwwfHx8&sdata=bXF5UU9DY3p0MkF5MFVwYkVTWFNMWXlkVFZFLzZYbkFmdnZCeldzcStXUT0%3d)) includes the following key responsibilities: 

* Implement data flows to connect operational systems, data for analytics and business intelligence (BI) systems
* Document source-to-target mappings
* Re-engineer manual data flows to enable scaling and repeatable use
* Support the build of data streaming systems
* Write ETL (extract, transform, load) scripts and code to ensure the ETL process performs optimally
* Develop business intelligence reports that can be reused
* Build accessible data for analysis

## Behaviours

As well as skills demonstrating behaviours at appropriate levels is an essential part of progression. The behaviours related to the data engineering role are:

* Making effective decisions
* Working Together
* Changing and improving
* Delivering at Pace
* Communicating and Influencing
* Leadership (some more senior roles only)

You can find descriptions of these behaviours and more information [here](https://www.gov.uk/government/publications/success-profiles/success-profiles-civil-service-behaviours).

# Development of this roadmap

This pathway was last reviewed October 2025. The next review is due October 2026. 

Community announcement 24/09/2026: 

:construction: This learning pathway is currently undergoing reconstruction :construction:


The following changes to this learning pathway *will be* made to better reflect the local ONS data engineer role profile:

* Testing will be absorbed into programming and build. 
* The information that was on the “Technical Understanding” page will be put on the homepage. 


Note that the current local ONS data engineering role profile does not currently match with the GDD Data Engineer role profile. We anticipate that more changes will eventually be made to the local role profile so that it better matches with the GDD one. Currently the profiles have the following differences: 

* The GDD role profile contains a skill called data compliance and security. The local role profile does not. 
* The local role profile contains a skill called “community collaboration” the GDD profile does not. There is no page on this learning pathway for community collaboration at this time. 

