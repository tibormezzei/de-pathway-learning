[Awareness](#awareness): understand and use basic data products that work on small datasets data in common formats 

[Working](#working-and-practitioner): design, build and test data products based on feeds from multiple systems, using a range of different storage technologies, access methods or both. Create repeatable and reusable products.

[Practitioner]((#working-and-practitioner)): design, build and test data products that are complex or large scale. Build teams to complete data integration services.

[Expert](#expert): establish enterprise-scale data integration procedures across the data development life cycle, and ensure that teams adhere to them
manage resources to ensure that data services work effectively at an enterprise level.

The table below shows which skill level each grade should be working at within three to six months of starting a new role.

**Grade** |Associate Data Engineer (EO) |Data Engineer (HEO) |Senior Data Engineer (SEO) |Head of Data Engineering (G7) |Lead Data Engineer (G6)
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
**Skill level** |TBD |Working |Practitioner |Expert |Expert 

# Awareness

[Pandera](https://pandera.readthedocs.io/en/stable/index.html) and [Great Expectations](https://docs.greatexpectations.io/docs/) are popular Python libraries for performing data validation.

[Article: Introduction to Pandera and Great Expectations](https://endjin.com/blog/2023/03/a-look-into-pandera-and-great-expectations-for-data-validation)

[Learning hub: Jenkins](https://learninghub.ons.gov.uk/course/view.php?id=543)

# Working and Practitioner

At Working level, colleagues should be able to work on the tasks below with assistance from a senior Data Engineer who may delegate the tasks. At Practitioner level, colleagues should be able to plan, design and build a process that brings data from multiple sources together into a unified structure (such as a data warehouse or data lake) to support analysis, reporting and business decision making.
The life cycle of a data integration project at practitioner level could follow the process below:

1. Define Business Objectives

* What questions should the data warehouse answer?
    * For instance, "Whats the survey response rate by interviewee demographic?"
* Who will the users of the data warehouse/ data lake be?
* What are the KPIs (Key Performance Indicators)

2. Identify and Analyse Source Systems

Inventory all existing systems that manage or interact with stakeholder data. Assess each source for structure, update frequency, accessibility and data quality.

3. Define Data Requirements:

Work with customers/researchers/analysts to define which data variables are needed from each system, required historical depth, and level of granularity for reporting.

This will require the development of:

* Data Dictionary: A detailed document listing
    * Each required data variable
    * Source system
    * Data Type
    * Description/purpose
    * Sample values
    * Any transformations required
    * Historical Depth:
        * How far back in time the users need the data
        * Some systems might not retail old data, so gaps will need to be noted.
    * Granularity – Level per detail for (examples):
        * Per interviewer
            * Per interview
            * Per day/week/month
    * Business Rules:
        * Derived fields
        * Standardisation
        * Normalised dates

4. Design Data Model:

Design the logical and physical schema for the data warehouse, selecting between star and snowflake schema depending on business needs. Identify fact and dimension tables. [Difference between Star Schema and Snowflake Schema | GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-star-schema-and-snowflake-schema/)

5. Select Technology Stack:

Evaluate and select appropriate tools and platforms for the data warehouse, ETL processing and reporting based on business scale, budget, and existing tech.

For instance, ETL processing might be conducted in Cloudera in DAP, Apache Airflow in GCP and VS Code on a local machine.

For the Data Warehouse itself (for storage and query engine), you might consider using BigQuery for GCP, or HUE Hadoop for Cloudera.

6. Design ETL Process:

Design and document the data extraction, transformation and loading workflows. Define data cleansing rules, scheduling, and failure handling logic.

7. Establish Data Governance & Quality Standards

Define policies for data ownership, access control, data privacy (PII), validation and quality checks. Ensure alignment with compliance requirements (such as GDPR). See the [DAMA-DMBOK2](../../Forms/Guidance%20Documents.aspx?q=dama+dmbok&id=%2fsites%2fDataArchitecture%2fDocuments%2fData+Architecture%2fDocuments%2fDAMA-DMBOK2-Enterprise-Version_5f64b1115fc0f_e.pdf&viewid=8160c651-771c-437e-95b0-f348c9f6ad51&parent=%2fsites%2fDataArchitecture%2fDocuments%2fData+Architecture%2fDocuments&parentview=7&xsdata=MDV8MDJ8TWljaGFlbGEuTGF3cmVuY2VAb25zLmdvdi51a3xjNzY0NTY5NWJhYzY0YTZjNDQ0MzA4ZGRjOTA2ZTFjNnwwNzg4MDdiZmNlODI0Njg4YmNlMDBkODExNjg0ZGM0NnwwfDB8NjM4ODg3NzUzNjI0OTM2MDg5fFVua25vd258VFdGcGJHWnNiM2Q4ZXlKRmJYQjBlVTFoY0draU9uUnlkV1VzSWxZaU9pSXdMakF1TURBd01DSXNJbEFpT2lKWGFXNHpNaUlzSWtGT0lqb2lUV0ZwYkNJc0lsZFVJam95ZlE9PXwwfHx8&sdata=NTY2anRqTEVVZUFKb2lHaTlmWlk3RU1TSERlOFpNUlhyZlRmV2l0WG1JYz0%3d) Ch3 for data governance considerations. 

8. Build Prototype/ Proof of Concept:
Develop a minimum viable product of the data warehouse using a subset of data and key reports to validate architecture, data model and stakeholder's expectations.

9. Plan for Scalability and Maintenance
Document long-term scalability strategies for data volume and user growth. Define maintenance, monitoring, alerting, and disaster recovery strategies.


# Expert

All of the criteria found in practitioner level with the ability to also develop materials and training sessions for stakeholders to understand and use the data warehouse, BI tools, and reporting dashboards.



