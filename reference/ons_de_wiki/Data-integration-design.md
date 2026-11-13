Data integration involves combining data from different sources to provide a centralised view to help produce, transform and test data related products. Analytics, reporting and operations that rely on data from multiple systems are dependent on a well designed Data Integration design.  An ONS specific example would be the Management Information system for Social Surveys, which has input data from various sources including Fusion, T-Mobile, reference data in Shared Drive and an app called Blaise and integrating into a data warehouse.  The awareness level of the skill is currently not defined in the GDD framework but we include resources here to get started with this skill. 

The table below shows which skill level each grade should be working at within three to six months of starting a new role.

**Grade** |Associate Data Engineer (EO) |Data Engineer (HEO) |Senior Data Engineer (SEO) |Head of Data Engineering (G7) |Lead Data Engineer (G6)
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
**Skill level** |TBD |Working |Practitioner |Expert |Expert 

# Awareness

[Awareness](#awareness): explain the basics and benefits of data integration design.

Skills:

* Basic knowledge of data formats (CSV, Excel, JSON)
* Be able to manually merge data using spreadsheets
* Understand what APIs and databases are (at a high level)
* Awareness of issues such as duplicates or mismatched IDs.

Tools: Excel

Informal learning:

[Learning Hub: Awareness of Data Linkage](https://learninghub.ons.gov.uk/course/view.php?id=1190) – Even data engineers who do not belong to the sub role of linkage engineer will need awareness level in data linkage.

# Working

[Working](#working): deliver data solutions in accordance with agreed organisational standards that ensure services are resilient, scalable and future-proof. Be able to write scrips/code for integration. 

Skills:
-	Be able to use Python/Pyspark/SQL to join or merge data
-	Understand primary keys, foreign keys and joins
-	Can pull data from databases

Tools: Python (Pandas), SQL, PySpark

Informal learning:

* [Learning Hub: Introduction to Data Linkage](https://learninghub.ons.gov.uk/course/view.php?id=1209)
* [Learning Hub: Data Linkage in Python](https://learninghub.ons.gov.uk/course/view.php?id=1212)

# Practitioner

[Practitioner](#practitioner): select and implement the appropriate technologies to deliver resilient, scalable and future-proofed data solutions. Be able to build scalable integration pipelines.  

Skills:
-	Design ETL pipelines that combine data from multiple sources
-	Resolve schema mismatches and handle slowly changing dimensions
-	Implement data mapping and transformation logic
-	Use orchestration tools and monitor data flows.

Tools: Custom ONS packages including Plumb-ELT, DE Utils, and DLH Utils, and Apache Airflow (for GCP)

Informal learning: 

[Cloud Skills Boost Course: Building Batch Data Pipelines on Google Cloud](https://www.cloudskillsboost.google/course_templates/53?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=49375693). This is a long course (approximately 12 hours) it covers everything from beginner questions such as "What is an ETL pipeline?" up to "How do I facilitate a multi service ETL pipeline on GCP".

ONS colleagues will probably want to follow the Python track over the Java track. 

[Cloud Skills Boost Lab: Writing an ETL Pipeline using Apache Beam and Dataflow (Python)](https://www.cloudskillsboost.google/focuses/64780?catalog_rank=%7B%22rank%22%3A2%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=49375504)

[Cloud Skills Boost Lab: Basic Airflow lab](https://www.cloudskillsboost.google/focuses/3528?catalog_rank=%7B%22rank%22%3A2%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=49375803)


# Expert

[Expert](#expert): Establish standards, keep them up to date and ensure adherence to them and keep abreast of best practice in industry and across government.

Skills:
-	Architects batch integrations (possibly also real-time integrations but unaware of ONS conducting real-time integration).
-	Designs for scalability, security and compliance
-	Governs metadata, data lineage and change data capture (CDC)

Tools: Kafka, Snowflake, Cloud Composer (GCP)



# General resources

We have a few in house tools and standards which are useful at all levels of this skill. 

### ons-python-template

At the more fundamental level we have an ONS Python project template.

Link: [ONSdigital/ons-python-template](https://github.com/ONSdigital/ons-python-template)

### De-Utils
Open-source Data Engineering utility package that contains useful functions when working with HDFS, Spark and ETLs. The functions in this repo are not tailored to a specific project and can be implemented for wider use. As the package is open source, anyone can contribute by either changing code or contributing a function they have made themselves.

Link: [ONSdigital/de-utils](https://github.com/ONSdigital/de-utils/tree/main)

### Plumb-etl

Python library that contains pipeline stages, transformers and utilities for creating ETL PySpark pipelines. Teams within Data Engineering in DEOD are in the process of integrating plumb-etl into their own data processes. Plumb-ETL can provide a standardised pipeline infrastructure, resulting in easier communication and staff transition between data engineering teams as well as a cross-team collaboration in maintaining and updating the infrastructure.

Link: [ONSdigital/plumb-etl: Library containing common PySpark ETL pipeline stages, transformers and various utilities.](https://github.com/ONSdigital/plumb-etl)

### DLH_Utils

Although this learning roadmap is supposed to be team agnostic, due to the wide need for data linkage across DGO teams we include here DLH_Utils. 

Link: [Data-Linkage/DLH_Utils: Library containing common profiling, cleaning and linkage functions](https://github.com/Data-Linkage/dlh_utils)


