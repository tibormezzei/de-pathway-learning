Problem management involves anticipating and identifying problems in systems, processes or services, and ensuring appropriate solutions are implemented.

* [Awareness](#awarness): Investigate problems in systems, processes, and services, with an understanding of the level of a problem, for example, strategic, tactical or operational. Contribute to the implementation of remedies and preventative measures.
* [Working](#working): Initiate and monitor actions to investigate patterns and trends to resolve problems effectively. Consult specialists where required, determine the appropriate resolution, and assist with its implementation. Determine preventative measures.
* [Practitioner](#practitioner): Ensure that the right actions are taken to investigate, resolve, and anticipate problems. Co-ordinate the team to investigate problems, implement solutions, and take preventive measures.
* [Expert](#expert): Anticipate problems and defend against them at the right time. Understand how a problem fits into the larger picture. Identify and describe problems, and help others to describe them. Build problem-solving capabilities in others. 

The table below shows which skill level each grade should be working at within three to six months of starting a new role.

**Grade** |Associate Data Engineer (EO) |Data Engineer (HEO) |Senior Data Engineer (SEO) |Head of Data Engineering (G7) |Lead Data Engineer (G6)
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
**Skill level** |TBD |Awareness |Working |Practitioner |Expert 

As well as covering problem solving at the smaller scale (e.g. in code), this section also covers [Agile](#agile-for-data-engineers). Agile can be used as a way to solve problems on a bigger scale e.g. delivering projects. 

It is difficult to distinguish between _awareness_ and _working_ for this skill. It is also difficult to distinguish between _practitioner_ and _expert_. The general resources section makes up the bulk of this page. We include logging in the practitioner section because knowledge and use of logging wouldn't normally be expected for more junior colleagues, although it may benefit junior colleagues to have an awareness of how to read logs. 

# General Resources 

What happens when your code doesn’t work? – or worse, stops working!

What will you do? Where will you turn? First things first, take a screen break!

Here are a few techniques relevant to problem resolution that you can try to troubleshoot your code and hopefully get it working:

### Making use of Print Statements :paw_prints:

Adding a simple [print statement](https://dev.to/nickjj/using-print-statements-are-a-handy-way-to-debug-and-explore-code-54ne) into your code can be a great way to get started on de-bugging. For example, adding something like `print('here!')` or `print('is this working?')` into your code to check if the code is reaching a particular point before failing / looping can help you pinpoint the problem. 

`print('here!')`

### Rubber Ducking :duck:

If you have never heard of rubber ducking, it is simply telling your problems to a rubber duck (other rubber animals and pets also work well). Essentially the idea is to say your problem aloud – explain it to someone who doesn’t understand (like a rubber duck). This forces you to explain the problem in detail and helps you to break it down.

[Here](https://rubberduckdebugging.com/) is some more information about rubber ducking. 

And a [virtual rubber duck](https://rubberduckdebugging.com/cyberduck/) (in case you don’t have one)

If that feels a bit silly, [here is a blog post about breaking the problem down without animal exploitation](https://nickjanetakis.com/blog/breaking-down-problems-is-the-number-1-software-developer-skill)

### Documentation :ledger:

Speaking of future proofing your code, let's talk about Documentation. Similarly to rubber ducking, writing good documentation for your code forces you to break the code down into smaller, manageable pieces.

There are many different documentation methods, from simple inline comments within your code. These can act as a reminder for your future self and help colleagues who may need to use/edit your code in the future. At the other end of a spectrum, you might consider including a `.README` file with any code packages. This might seem more formal but fulfils many of the same functions. Great resources for documentation include [The Aqua Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) (formerly known as the duck book); [the Real Python guide to documenting Python code](https://realpython.com/documenting-python-code/); and [Upsun blog](https://upsun.com/blog/code-documentation/#:~:text=As%20your%20software%20evolves%2C%20missing,project%E2%80%94even%20with%20complex%20logic).

### Pair Programming :dancers:

If you are feeling lost and all alone with your code problems, reach out to a colleague and ask to do some Pair Programming. These can be formal or informal sessions, and there are a number of ways to approach this – they all essentially involve working together and screen sharing to problem solve. Some common types of pair programming are listed below:

• Driver-Navigator: One person drives (types the code) and the other navigates (tells them what to write where).

• Ping-Pong: Common in TDD (Test Driven Development). One person writes a test and the other makes it pass.

• Unstructured: Book some time with a colleague, grab a coffee, screenshare and problem solve together.

For more detail here are some blogs you could read about pair programming: [datadoghq](https://www.datadoghq.com/knowledge-center/pair-programming/), [Code Academy](https://www.codecademy.com/resources/blog/what-is-pair-programming/).

### Artificial intelligence :robot:

What are the best practices when using AI to help solve technical problems? The answer to this question will no doubt continue to change as AI evolves, and you will likely get different answers from different developers. However, we think there is once consistent message - AI should not replace critical thinking. 

What can AI do well when it comes to writing code? 
- AI can create a set of parametrised tests for your code, but you should check the tests to ensure they are actually what you want to code to do. 
- AI can create docstrings when you have writers block, but you should always ensure the docstring is an accurate description of the code. 
- AI can explain code that you don't understand. 

What can go wrong?
- AI can hallucinate (for example provide references that don't exist).
- AI can misunderstand your prompt and write code that runs but doesn't do what you intended.

See [this Pluralsight blog post](https://www.pluralsight.com/resources/blog/business-and-leadership/AI-in-software-development) for more information on AI's strengths and weaknesses when it comes to software development.  

Whatever you use AI for at work, it is your responsibility to familiarise yourself with [ONS policy](https://officenationalstatistics.sharepoint.com/:w:/r/sites/knexPolicies/_layouts/15/doc2.aspx?sourcedoc=%7B054F0B07-1984-4ADD-B2F5-4C015FC43265%7D&file=UKSA%20Artificial%20Intelligence%20(AI)%20Policy%20v1.0%201.docx&action=default&mobileredirect=true&DefaultItemOpen=1) on AI use, and you should know what tools are allowed. At the time of writing, we are permitted to use GitHub Copilot, Microsoft Copilot, and Gemini (if using GCP, keep an eye on the bill) but this may change. We can use on our on-network laptops is GitHub copilot in VS Code. You may find the line completion useful or annoying. You may prefer to use GitHub copilot chat instead. 

# Roles and Agile for Data Engineers

In DGO, most teams will use JIRA as a project management tool. There are some differences between Jira and other project management tools e.g. GitHub, so we recommend learning about Jira specifically. See [the official Jira product guide](https://www.atlassian.com/software/jira/guides/getting-started/introduction#what-is-jira-software).

[Here](https://learninghub.ons.gov.uk/course/view.php?id=682) is a link to the project delivery learning suite. A data engineer won't need to know everything in this area about Agile and Project Delivery, however the learning suite for Project Delivery is in a mature state so there will be many resources there that data engineers will find useful and relevant to their role. 

Another general Agile learning resource is the [Agile Percipio channel](https://ons.percipio.com/channels/e4be53b0-f9ee-11e6-9896-0776e4b35762?tab=WATCH). 

As well as working with colleagues who take on the standard Agile project management roles we also have a couple of other important roles to be aware of when working in any ONS data team. 

The first role is DisCO and you can find DisCO training on the [Learning Hub](https://learninghub.ons.gov.uk/course/view.php?id=659). The term Disco comes from "Disclosure Control" and the idea of the role is to oversee the movement of sensitive data to outside of secure environments e.g. to prepare for publication.

The second role is an Information Asset Owner (IAO), they are responsible for approving data use-cases e.g. for statistical or operational purposes. 

For more information about these roles, and other roles associated with them, please search them on the intranet.    

# Awareness 

At the _awareness_ level you should:
1. Understand problems that arise e.g. by understanding error messages. You should be able to understand the severity of a problem and potential knock-on effects.
2. Understand some of the techniques for problem solving code and infrastructure and why they might be beneficial and their limitations. 
3. Have a basic understanding of possible risks and what techniques could be used as preventative measures. See also [[Testing]].
4. Have a basic understanding of Agile and its benefits and drawbacks compared to waterfall project management. 

At awareness level you should be able to use tests and logging to understand and help solve simple problems, although there is no expectation that you should be able to create your own logger. See also [[Testing]] and [Logging](#logging-evergreen_tree)

# Working 

At the working level you should be able to understand all the problem-solving methods mentioned in the general resources section and you should have implemented them (where appropriate) yourself. You should have completed some work in a team who are using Agile methodology for project planning and should have a solid understanding of your team's workflow.  

# Practitioner

### Logging :evergreen_tree:

The next step, for more complex problems might be Logging. Setting up a logger for your code can be a great way to introduce continuous improvement and future proof your code. Here are some starting points for logging in PySpark: [Spark documentation](https://spark.apache.org/docs/4.0.0-preview2/api/python/development/logger.html), and [Medium blog post](https://polarpersonal.medium.com/writing-pyspark-logs-in-apache-spark-and-databricks-8590c28d1d51).

For logging monitoring and observability on GCP please see [cloud skills boost](https://www.cloudskillsboost.google/catalog?utf8=%E2%9C%93&keywords=logging&_gl=1*w6adtr*_up*MQ..*_ga*MTUzNDI5MjM1NC4xNzQxNzA3OTQ5*_ga_2X30ZRBDSG*MTc0MTcwNzk0OC4xLjAuMTc0MTcwNzk0OC4wLjAuMA..). 

At the practitioner level you should be able to help others understand how to solve problems, and you should also have a familiarity with logging. This includes not only reading and understanding logs, but also setting up a logger yourself. You should also be comfortable with Agile and have a solid understanding of all roles in Agile project management and how they differ.   

# Expert

At the _expert_ level you should be able to lead a team with varying levels of experience in the implementation of problem solving. You should be comfortable with setting up logging, monitoring and observability for multiple systems. 

At the expert level, data engineers may also want to consider some more [in depth, agile training](https://www.thescrummaster.co.uk/courses/ultimate-agile-elearning-course/) and/or [scrum training](https://www.thescrummaster.co.uk/courses/ultimate-scrum-course/). Although generally we work with delivery managers, this sort of training may lend itself to understanding the bigger picture, identifying and describing problems, and helping others to describe them, and building problem-solving capabilities in others.

