🚧 This page is currently undergoing construction. Testing has been merged with programming and build. More updates to follow. 🚧 

Programming and build (data analytics and engineering) involves working with code across the software development life cycle, following modern development standards and practices, test automation, build pipelines and repeatable deployment processes, to implement secure, maintainable software solutions.

* [Awareness](#awareness): develop code under supervision using simple tools and languages and explain the value of development standards.
* [Working](#working): design, code, test, correct and document simple programs or scripts under the direction of others.
* [Practitioner](#practitioner): use agreed standards and tools to design, code, test, correct and document moderate-to-complex programs and scripts from agreed specifications and subsequent iterations. Collaborate with others to review specifications where appropriate.
* Expert: set local or team-based standards for programming tools and techniques and can select appropriate development methods. Advise on the application of standards and methods and ensure compliance. Take technical responsibility for all stages and iterations in a software development project, providing method-specific technical advice and guidance to project stakeholders.

The table below shows which skill level each grade should be working at within three to six months of starting a new role.

**Grade** |Associate Data Engineer (EO) |Data Engineer (HEO) |Senior Data Engineer (SEO) |Head of Data Engineering (G7) |Lead Data Engineer (G6)
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
**Skill level** |Working |Working |Practitioner |Expert |Expert 

# General resources

If you are looking for some beginners tutorials on using Python please have a look at [Data analysis and synthesis](https://github.com/MichaelaLawrenceONS/test_wiki/wiki/Data-analysis-and-synthesis) awareness. 

Working in data engineering isn't just about writing code that works, its about writing code that works efficiently. In this page we include some resources which detail techniques and methods which can help with this. 

If you are looking for training that leads to [certification on GCP](https://cloud.google.com/learn/certification?hl=en) you may be able to take part in the Google Get Certified Program. 

For some general git training across a range of topics on Git and GitHub please see [GitHub Skills](https://skills.github.com/)

## IDEs

If you are going to want to start writing Python you are going to need something to write it on this is where integrated development environments (IDEs) come in. You will probably be using one or more of these: 
* Visual Studio Code (or VS Code for short). You can install VS Code on your ONS laptop by logging a service desk request for the software and then downloading and installing via the software center. [Here](https://www.youtube.com/watch?v=E9U-EBG8jVk) is some basic introductory training on how to use VS Code to write Python.
* Jupyter Notebooks (or similar notebook type interfaces). These must be installed by requesting Python on the service desk and then follow the [ASAP wiki](https://gitlab-app-l-01/ASAP/coding-getting-started-guide/-/wikis/home). [Learning Hub: Python - Jupyter Notebooks Overview](https://learninghub.ons.gov.uk/course/view.php?id=1225).
* Spyder. As with Jupyter Notebooks you install Spyder using the service desk and the ASAP wiki. [YouTube: basics of Spyder](https://www.youtube.com/watch?v=WV9bm4ey7Cg&list=PLPonohdiDqg9epClEcXoAPUiK0pN5eRoc&index=2)

## Concepts

An overview of the philosophy of Python programming can be found in [PEP 20: The Zen of Python](https://peps.python.org/pep-0020/). See [PEP 8](https://peps.python.org/pep-0008/) for a more detailed style guide. 

The ability to write object oriented code is a key feature of Python. Here is a short video comparing functional programming with object oriented programming, [YouTube: FP vs OOP](https://www.youtube.com/watch?v=08CWw_VD45w).

[Learning Hub: Command line basics](https://learninghub.ons.gov.uk/course/view.php?id=494) you can also use this [list](https://www.geeksforgeeks.org/linux-vs-windows-commands/) if you switch between using Windows and Linux commands often and need to translate. 

## Testing

[PyTest](https://docs.pytest.org/en/stable/) is probably more commonly used in the ONS than the inbuilt unittest module or Robot. They have plenty of how to guides and information on their website. 

[Writing good unit tests in Python with Ease](https://mitches-got-glitches.medium.com/writing-good-unit-tests-in-python-with-ease-5fb6d7aa2b77) - starts with “why test”, then goes into details.

Test driven development (TDD) could probably be considered a practitioner or expert level topic however the concepts of TDD can be beneficial to even beginner testers. There are lots of resources out there for TDD [IBM](https://developer.ibm.com/articles/5-steps-of-test-driven-development/) and [Test Driven Data Analysis (TDDA)](https://www.tdda.info/pages/about.html) are a couple of options. We don't encourage the use of the TDDA library necessarily but the blog itself is very useful for understanding TDD concepts from a data perspective as opposed to a software perspective.

# Awareness

## Pipelines

Infrastructure as code is often considered a more advanced topic. We often first learn how to use infrastructure using point and click on the GCP console or equivalent. We include a short introduction to Terraform here, [YouTube: Getting started with Terraform for Google Cloud](https://www.youtube.com/watch?v=BUPenAjobjw&pp=ygUhaW50cm9kdWN0aW9uIHRvIHRlcnJhZm9ybSBmb3IgR0NQ)

A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. As data engineers in the ONS we mostly use [Docker](https://docs.docker.com/guides/docker-overview/) for containerisation.  

[YouTube: Containerize Python Applications with Docker](https://www.youtube.com/watch?v=0TFWtfFY87U)

[YouTube: Logging](https://www.youtube.com/watch?v=pxuXaaT1u3k)

[Learning Hub: Introduction to Continuous Integration](https://learninghub.ons.gov.uk/course/view.php?id=568)

At the ONS we use Git, along with GitHub and GitLab for version control. Version control is a part of writing reproducible analytical pipelines (RAPs). 

* [Learning Hub: Packaging and Documentation](https://learninghub.ons.gov.uk/course/view.php?id=1212) 
* [Article: What is Git? Our beginner’s guide to version control](https://github.blog/developer-skills/programming-languages-and-frameworks/what-is-git-our-beginners-guide-to-version-control/)
* [Learning Hub: Introduction to RAP](https://learninghub.ons.gov.uk/course/view.php?id=1236)
* [Learning Hub: Loops and Functions](https://learninghub.ons.gov.uk/course/view.php?id=1222)

Unit testing is also an important part of pipeline building with Python. You can find more about this in the [Working](#working) section. 

## GCP

There is a great series of YouTube videos where you can get a quick overview of GCP services called [Cloud Bytes](https://www.youtube.com/watch?v=CFw4peH2UwU&list=PLIivdWyY5sqIQ4_5PwyyXZVdsXr3wYhip). We include some here:
 
* [YouTube: Cloud Storage in a minute](https://www.youtube.com/watch?v=wNOs3LlsH6k&list=PLIivdWyY5sqIQ4_5PwyyXZVdsXr3wYhip&index=6)
* [YouTube: Cloud Functions in a minute](https://www.youtube.com/watch?v=BL4ZlPEamDo) You can also learn more about Cloud Tasks and Cloud Scheduler in this video. 
* [YouTube: Pub/Sub in a minute](https://www.youtube.com/watch?v=jLI-84UjZLE) There will be many data engineers in the ONS who have no need for Pub/Sub because they wont be streaming data.
* [YouTube: BigQuery in a minute](https://www.youtube.com/watch?v=CFw4peH2UwU&pp=ygUVQmlnIFF1ZXJ5IGluICBhbWludXRl)
* [YouTube: BigQuery ML in a minute](https://www.youtube.com/watch?v=0RMT8uEplbM) 
* [YouTube: Cloud IAM in a minute](https://www.youtube.com/watch?v=zd5d9Vv1ZFE&list=PLIivdWyY5sqIQ4_5PwyyXZVdsXr3wYhip&index=34)
* [YouTube: Cloud Logging in a minute](https://www.youtube.com/watch?v=hpUHZixlHiA&list=PLIivdWyY5sqIQ4_5PwyyXZVdsXr3wYhip&index=28)
* [YouTube: Cloud Monitoring in a minute](https://www.youtube.com/watch?v=7BLV24noNGc&list=PLIivdWyY5sqIQ4_5PwyyXZVdsXr3wYhip&index=28)
* [YouTube: Dataproc in a minute](https://www.youtube.com/watch?v=Jj6mp7Sam10)
* [YouTube: Dataplex in a minute](https://www.youtube.com/watch?v=bbFeAt7cw1g)

# Working

At working level you may already be familiar with some [Python design patterns](https://python-patterns.guide/) but for all the ones you are not familiar with you can use the link. 

[Learning Hub: DataFrames, Manipulation and Cleaning](https://learninghub.ons.gov.uk/enrol/index.php?id=484)

[Learning Hub: Introduction to Object Orientated Programming in Python](https://learninghub.ons.gov.uk/course/view.php?id=567)

[CS50P: Week 8 OOP](https://cs50.harvard.edu/python/2022/weeks/8/)

## Pipelines

* [Learning Hub: Introduction to Git](https://learninghub.ons.gov.uk/course/view.php?id=1165) 
* [Presentation: Make Git Happen]([https://josephcrispell.github.io/standalone/gov-uk-rap-materials_make-git-happen.html#1](https://josephcrispell.github.io/standalone/gov-uk-rap-materials_make-git-happen.html))
* [Game: Oh My Git](https://ohmygit.org/) for use on an off-network laptop only. 
* [Cheat Sheet: Git](https://education.github.com/git-cheat-sheet-education.pdf)
* [Learning Hub: Packaging Code with Python](https://learninghub.ons.gov.uk/course/view.php?id=533)

## GCP

[Cloud Skills Boost (10 credits): Dev Apps with Cloud Functions](https://www.cloudskillsboost.google/course_templates/505?catalog_rank=%7B%22rank%22%3A10%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=25614368)

## Testing
Testing involves ensuring that requirements have been fully met by using appropriate tools and techniques to verify that a product or service works. There are many different ways to classify tests. Unit tests are probably the best place to start but after that there are multiple directions you could go in. Here is a blog posts that describes [different types of testing in Python](https://www.bitecode.dev/p/testing-with-python-part-5-the-different). Beginners may also find some of the [earlier blog posts in this series](https://www.bitecode.dev/p/testing-with-python-part-1-the-basics) to be useful. At awareness level you should be able to run tests and possibly recognise different kinds of tests but not necessarily know how to write your own from scratch.   

CS50P has been mentioned elsewhere in this learning roadmap. See [CS50P: Week 5 Unit Tests](https://cs50.harvard.edu/python/2022/weeks/5/) for an overview of error handling and PyTest.

[YouTube: How to Write Unit Tests in Python](https://www.youtube.com/watch?v=YbpKMIUjvK8)

[Learning Hub: Introduction to Unit Testing](https://learninghub.ons.gov.uk/course/view.php?id=1171)

[Real Python: Getting started with testing in Python (PyTest)](https://realpython.com/python-testing/).

You can categorise unit tests in different ways. One way is [positive vs negative testing](https://www.geeksforgeeks.org/software-engineering/difference-between-positive-testing-and-negative-testing/). 

### Getting the right information when Pytest runs

Useful [PyTest command line options](https://adamj.eu/tech/2019/10/03/my-most-used-pytest-commandline-flags/)

Coverage reports with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/reporting.html)

# Practitioner 

[DAP CATS: Coding as a team](../../../anstanpi/CATS/Forms/AllItems.aspx?id=%2Fsites%2Fanstanpi%2FCATS%2FTraining%20and%20Guidance%2FRecorded%5Fpresentations%2FSpark%5Fat%5Fthe%5FONS%5FMarch%5F2022%2FCoding%20as%20a%20team%20%2D%20adopting%20best%20practice%20using%20Spark%2C%20R%2C%20Git%20and%20DAP&p=true&ct=1658139978159&or=Teams%2DHL&ga=1)

## Testing

[Article: Five Advanced PyTest Fixture Patterns](https://www.inspiredpython.com/article/five-advanced-pytest-fixture-patterns)

Ed's helpful demo of [PyTest Examples](https://github.com/EdCussONS/pytest_examples) is especially useful if you are interested in parameterised testing. 

[Book: Obey the testing goat](https://www.obeythetestinggoat.com/pages/book.html) - this is a slightly outdated implementation of building a simple, fully tested website with Python but the concepts are solid. 

[Book: Cosmic python](https://www.cosmicpython.com/book/preface.html) - this is the sequel to obey the testing goat and has some really useful concepts in it about the repository pattern and other things that aid testability - it's become my favourite python book!

[Video: Stop using mocks (for a while)](https://www.youtube.com/watch?v=rk-f3B-eMkI) PyCon talk by the author of obey testing goat and cosmic python about one of the best concepts from the book

[Video: Stop mocking start testing](https://www.youtube.com/watch?v=Xu5EhKVZdV8) - Talk by some google engineers about mocks and testing

 

