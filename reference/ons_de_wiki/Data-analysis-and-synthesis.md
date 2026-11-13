Data analysis and synthesis for a data engineer involves examining, interpreting and analysing data to help make informed decisions. The GDD framework only describes Working and Practitioner levels for data engineering. We have included descriptions for the Awareness and level here as well because of the wide range of data engineering skill levels we have at the ONS so that apprentices and colleagues coming from other professions can find appropriate resources.

* [Awareness](#awareness): explain the benefits of quantitative analysis, and how data profiling can be useful. 
* [Working](#working): undertake data profiling and source system analysis present clear insights to colleagues to support the end use of the data
* [Practitioner](#practitioner): understand and help teams to apply a range of techniques for data profiling source system analysis from a complex single source bring multiple data sources together in a conformed model for analysis

The table below shows which skill level each grade should be working at within three to six months of starting a new role.

**Grade** |Associate Data Engineer (EO) |Data Engineer (HEO) |Senior Data Engineer (SEO) |Head of Data Engineering (G7) |Lead Data Engineer (G6)
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
**Skill level** |TBD |Working |Working |Practitioner|Practitioner 

# General Resources

[Coffee & coding:](https://teams.microsoft.com/l/team/19%3AqULwEkDAmExr95ouE5mVDMRkzhF3uV8cMMYQRgbyw2U1%40thread.tacv2/conversations?groupId=8ad6b255-e0da-4d21-9659-5fdeca628904&tenantId=078807bf-ce82-4688-bce0-0d811684dc46) monthly casual meetings where projects are presented with time for Q&A at the end.

[RAP network:](https://teams.microsoft.com/l/team/19%3ANAmryVC2tshc8y25oB3SWGqr3WnPQqdC2BKL4n-cPGs1%40thread.tacv2/conversations?groupId=bc27c1c9-90f6-46f1-a84c-538dd144f4d7&tenantId=078807bf-ce82-4688-bce0-0d811684dc46) Similar to Coffee & Coding but focussed on reproducible analytical pipelines. On the topic of RAPs the best written resource is the [Aqua Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government).

For getting started with Python on ONS on net machines please see the [ASAP guide](https://gitlab-app-l-01/ASAP/coding-getting-started-guide/-/wikis/home) (note that you must be connected to the VPN to access the link).

At working and practitioner levels you will probably start to use PySpark and so readers may also find the [DAP Community](https://teams.microsoft.com/l/team/19%3Ag3-Yeok2ZR0VrWVIsFGckW98185Tv8tuZ-jjHWhXR5Q1%40thread.tacv2/conversations?groupId=c11e29b1-4b16-495b-9090-dc22ce74ba0d&tenantId=078807bf-ce82-4688-bce0-0d811684dc46) a useful place to get information.

And of course there is always [viva engage](https://engage.cloud.microsoft/main/org/officenationalstatistics.onmicrosoft.com/groups/eyJfdHlwZSI6Ikdyb3VwIiwiaWQiOiI0OTM0Nzc2NDIyNSJ9/new) if you need to ask for help because you can't find your answer elsewhere.

# Awareness

Data analysis and synthesis is a skill separate from programming and build but in practice all data engineers will be expected to use Python or another programming language to perform data analysis and synthesis. In this section we will cover the creation of statistics and data profiling using common Python libraries and SQL. 

At the level of awareness you should be able to explain the benefits of quantitative analysis, and how data profiling can be useful. 

**Concepts and command line basics**

[Learning Hub: Awareness of coding tools](https://learninghub.ons.gov.uk/course/view.php?id=1163) – this course will familiarise you with the basic principles of coding tools which are essential for a data engineer using data analysis. 

[Article: PySpark vs Pandas](https://www.codeconquest.com/blog/pyspark-vs-pandas-performance-memory-consumption-and-use-cases/) – working in the ONS, especially whilst working on DAP you will often have to choose between using PySpark or Python Pandas to write code.

[Learning Hub: Command line basics](https://learninghub.ons.gov.uk/course/view.php?id=1166) you can also use this [list](https://www.geeksforgeeks.org/linux-vs-windows-commands/) if you switch between using Windows and Linux commands often and need to translate. 

**IDEs**

If you are going to want to start writing Python you are going to need something to write it on this is where integrated development environments (IDEs) come in. See [Programming and Build section on IDEs](https://github.com/ONSdigital/DRAFT_DE_learning_roadmap/wiki/Programming-and-build-(data-engineering))

**Data profiling**

[Article: Data profiling](https://www.ibm.com/topics/data-profiling) this resource was recommended to the apprentices by DAB when they were first getting started with data profiling. 

# Working

You know how to undertake data profiling and source system analysis and can present clear insights to colleagues to support the end use of the data.

**SQL**

SQL is an essential tool for any data engineer and can often be easier and quicker to use for very simple data queries compared to Python. It is also the foundational language on which the Google BigQuery dialect is built on. 

[Learning Hub: Foundations of SQL](https://learninghub.ons.gov.uk/course/view.php?id=1162) – recently this course was reviewed as being a good introduction but quite text heavy. Have a look at [SQLite Online](SQLiteOnline.com) to have a go at some "doing" alongside this course. You might also consider installing SQL on your personal laptop whether you do that or not this 3-hour [YouTube course](https://www.youtube.com/watch?v=7S_tz1z_5bA) will be useful to any SQL beginners. 

[SQL Noir](https://www.sqlnoir.com/) - a fun way to learn some SQL. 

[SQL Premier League](https://sqlpremierleague.com/) - similar to the above but focussed on sports (lots of sports not just football). 

**Python and PySpark**

An overview of the philosophy of Python programming can be found in [PEP 20: The Zen of Python](https://peps.python.org/pep-0020/). See [PEP 8](https://peps.python.org/pep-0008/) for a more detailed style guide.

[Learning Hub: Python - DataFrames, Manipulation, and Cleaning](https://learninghub.ons.gov.uk/course/view.php?id=1156)

[Learning Hub: Data Visualisation in Python](https://learninghub.ons.gov.uk/course/view.php?id=1195) Data visualisation is not something that a data engineer should expect to master but it’s good to be able to create quick plots for the purposes of understanding. 

[Learning Hub: Introduction to PySpark](https://learninghub.ons.gov.uk/course/view.php?id=1161) again PySpark isn’t necessary for the theory behind data analysis and synthesis but at the ONS it has been essential and the language of choice for large-scale data processing in a distributed environment.

**Data profiling in Python**

[ydata-profiling:](https://github.com/ydataai/ydata-profiling) this isn't really a learning resource but its a nifty package to do some quick data profiling of a pandas dataframe. It also works in PySpark.

**Data Synthesis**

Occasionally as data engineers we are asked to generate synthetic or dummy data for customers or to use as tests for our pipelines. The distinction between dummy and synthetic data is dummy data will probably not closely resemble distributions found in the real data (unless you hard code that in) synthetic data may share properties (such as distributions of variables) with the real data. Both types of data could have the same columns as the real data. Here are a few simple options for generating some simple dummy or synthetic data. *Top tips: Don't assume synthetic data is 100% private, the synthetic data may or may not resemble the real data in distributions and distributions themselves may be sensitive. Secondly always label your synthetic or dummy data as such.* 

To generate some simple dummy data you could use [Mockaroo](https://www.mockaroo.com/). 

Another option for generating dummy data on your machine would be [faker](https://pypi.org/project/Faker/).

A fairly simple option for generating some synthetic data is [SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html). SMOTE is normally for balancing datasets with unbalanced categories. You can create a new column containing one of two values "real" or "dummy". Label all real data as such and create a "dummy" dataset to be appended the end of your dataframe which has twice as many rows and the same columns as your real data. Filling "dummy" with zeros. Then use SMOTE to simulate some more "real" data to balance the categories.

There are many more ways of generating dummy or synthetic data but always follow the two top tips above whatever method you choose. 

# Practitioner

[Learning Hub: Intermediate Level Spark](https://learninghub.ons.gov.uk/course/view.php?id=583)