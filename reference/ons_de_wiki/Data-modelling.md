Data modelling is the process of creating a visual representation or abstraction of an organisation's data and its relationships. It involves defining the structure of the data to be stored in a database or other data storage system. The primary purpose of data modelling is to facilitate a clear understanding of the data, its relationships, and how it supports business processes.

Although data modelling should be a part of data engineers remit in DGO we are in the privileged position of working alongside data architects who often know a lot more on the subject. This page was put together with the help of resources provided by the DAB team and their learning pathway. We mostly use Erwin data modeler at the ONS so some resources focus on this specific software. 

[Awareness](#awareness): show an awareness of different data models and tools, and understand when they could be used. Show an awareness of industry-recognised data modelling patterns and standards.

[Working](#working): explain the concepts and principles of data modelling. Produce, maintain and update relevant data models for an organisation’s specific needs. Reverse-engineer data models from a live system.

[Practitioner](practitioner): produce relevant data models across multiple subject areas. Explain which models to use for which purpose. Understand industry-recognised data modelling patterns and standards, and when to apply them. Compare and align different data models

[Expert](expert): understand the concepts and principles of data modelling and can produce relevant data models. Work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations. Design the method to categorise data models within an organisation. 

In the current role template data modelling is considered a desirable and not an essential skill for data engineers. The table below shows which skill level each grade should be working at within three to six months of starting a new role.

**Grade** |Associate Data Engineer (EO) |Data Engineer (HEO) |Senior Data Engineer (SEO) |Head of Data Engineering (G7) |Lead Data Engineer (G6)
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
**Skill level** |TBD |Working |Practitioner |Expert |Working 

# Awareness 

At awareness level you should: 
* be familiar with different types of entity-relationship data model (ERD - conceptual, logical physical)
* be able to read and understand a data model
* be able to explain the benefits of using a data model for the purposes of a particular project

[YouTube: Introduction to Data Modelling](https://www.youtube.com/watch?v=qKWnFRnjkA0) (2:20)

# Working

At working level you should:
* be able to identify which type of data model would Be appropriate for a given situation and/or audience
* be able to seek information for the creation of data models via research and stakeholder engagement
* be familiar with different types of data structure: relational, dimensional, tree, object oriented
* be able to create conceptual and logical data model based on relevant business information
* be able to explain the benefits of using a data model for on going maintenance and use of a data asset
* be familiar with different types of data model notation, e.g. ERD and UML
* understand the principles of database normalisation.
At this level of skill you should be the stage where you are starting to build or maintain very simple data models yourself.

[Percipio: (Book) Hoberman - Data Modelling Made Simple](https://dew1-share.percipio.com/cd/zlNcAFJCE): this may have to be acquired from somewhere other than Percipio. 

[YouTube Playlist: Erwin Data Modeler Tutorial](https://www.youtube.com/playlist?list=PLdWyZdkgKpTWy_24ldyMY0vLEfTS_5eYP): this resource is a little old but should still be useful for the basics. 

[Poolparty resource library](https://www.poolparty.biz/resource-library)

# Practitioner

At the practitioner level you should:
* be able to validate a data model
* be able to design a physical data model from a logical data model, for particular technologies
* be able to apply a data model to aid data migration, integration, extraction and acquisition
* be able to check that a model adheres to the standards for data modelling which are expected

The [BCS certificate in systems modelling](https://www.bcs.org/qualifications-and-certifications/certifications-for-professionals/solution-development/bcs-practitioner-certificate-in-systems-modelling-techniques/) is not free and it is not going to be required anywhere in DGO but we have included the website as a resource here because you can find some useful free resources there. See also chapter 5 of the [DAMA-DMBOK2](../../Forms/Guidance%20Documents.aspx?q=dama+dmbok&id=%2fsites%2fDataArchitecture%2fDocuments%2fData+Architecture%2fDocuments%2fDAMA-DMBOK2-Enterprise-Version_5f64b1115fc0f_e.pdf&viewid=8160c651-771c-437e-95b0-f348c9f6ad51&parent=%2fsites%2fDataArchitecture%2fDocuments%2fData+Architecture%2fDocuments&parentview=7&xsdata=MDV8MDJ8TWljaGFlbGEuTGF3cmVuY2VAb25zLmdvdi51a3xjNzY0NTY5NWJhYzY0YTZjNDQ0MzA4ZGRjOTA2ZTFjNnwwNzg4MDdiZmNlODI0Njg4YmNlMDBkODExNjg0ZGM0NnwwfDB8NjM4ODg3NzUzNjI0OTM2MDg5fFVua25vd258VFdGcGJHWnNiM2Q4ZXlKRmJYQjBlVTFoY0draU9uUnlkV1VzSWxZaU9pSXdMakF1TURBd01DSXNJbEFpT2lKWGFXNHpNaUlzSWtGT0lqb2lUV0ZwYkNJc0lsZFVJam95ZlE9PXwwfHx8&sdata=NTY2anRqTEVVZUFKb2lHaTlmWlk3RU1TSERlOFpNUlhyZlRmV2l0WG1JYz0%3d) and this [group of Erwin specific resources](https://officenationalstatistics.sharepoint.com/:x:/r/sites/DataArchitecture/_layouts/15/Doc.aspx?sourcedoc=%7bEC9706DB-0AC1-430A-8843-33C02A4EAC69%7d&file=Erwin+Documentation+Catalog.xlsx&action=default&mobileredirect=true&xsdata=MDV8MDJ8TWljaGFlbGEuTGF3cmVuY2VAb25zLmdvdi51a3xjNzY0NTY5NWJhYzY0YTZjNDQ0MzA4ZGRjOTA2ZTFjNnwwNzg4MDdiZmNlODI0Njg4YmNlMDBkODExNjg0ZGM0NnwwfDB8NjM4ODg3NzUzNjI0OTUzNjA3fFVua25vd258VFdGcGJHWnNiM2Q4ZXlKRmJYQjBlVTFoY0draU9uUnlkV1VzSWxZaU9pSXdMakF1TURBd01DSXNJbEFpT2lKWGFXNHpNaUlzSWtGT0lqb2lUV0ZwYkNJc0lsZFVJam95ZlE9PXwwfHx8&sdata=NlBlalQ0bEw0dXRGRlBZM0Rrb0lzWjVvNWVXTnl0LzVvVTY2dlN0a3hjST0%3d) put together by DAB. 

# Expert 

At the expert level you should be able to lead on development and management of complicated data models and be able to reverse engineer a physical data model from a variety of databases e.g. SQL Server, Oracle, Hive, Excel etc. 
