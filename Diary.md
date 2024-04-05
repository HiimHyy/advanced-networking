# Background Check:
After spending the last 2 years working on several projects:
- Fullstack application: CRUD (Create, Read, Update, Delete) with lots of RESTful APIs usage.
- Programming languages:
	- JavaScript/TypeScript: mainly for web development.
	- Golang: simple backend to learn making requests.
	- Python: various application categories.
	- Dart(Flutter): mobile development.
- Tools:
	- Postman: making HTTPS requests.
	- Browser: review requests.
	- Git: version management.
	- Docker: deploy application.
	- PostgreSQL/MongoDB: database.

# Course overview:
## ETW-MDP Study Diary

As I embark on this journey through the ETW-MDP course, I've decided to keep a detailed diary of my experiences, learnings, and reflections. This diary will not only serve as a personal log of my progress but also as a testament to the challenges and achievements along the way.

### Chapter 1: Introduction to Python and Programming Basics

#### Week 1: The Adventure Begins

##### **Getting Started**

My first week with the ETW-MDP course was an exciting mix of anticipation and new learnings. Chapter 1, titled **Introduction to Python and Programming Basics**, promised a comprehensive start to my programming journey, and it did not disappoint.

##### **Diving into Python**

With some prior experience in Python, I anticipated a smooth start. The chapter began with foundational concepts, an invitation to revisit the basics of Python for me. The initial sections, including **1.0 Introduction** and **1.1 Code and Communities of Practice**, were insightful, emphasizing the significance of coding communities such as GitHub and Stack Overflow. It was a reminder of the vast support network available to developers.

#### Activities and Reflections

- **Lab - PC Setup for Workshop**: Setting up my development environment was the first practical step. It felt good to prepare my tools, ensuring I was ready for the tasks ahead.

- **The Power of Code**: Reading about the impact of coding in various industries made me appreciate the path I've chosen. It's not just about writing code; it's about solving real-world problems.

#### Week 2: Into the Depths of Python

##### **Exploring Python Basics**

This week, I delved deeper into Python with **1.2 Python Basics**, tackling the intricacies of data types, variables, and basic programming constructs. Activities like using the Python interpreter and writing simple programs helped cement my understanding of the language's fundamentals.

##### **Hands-On Learning**

I particularly enjoyed the interactive nature of the lessons. From basic data types to more complex structures like lists and dictionaries, each section offered hands-on activities that challenged me to apply what I had learned.

##### Highlights:

- **If Functions and Loops**: Learning about control structures in Python was a highlight. The exercises on `if` statements and loops were particularly engaging, offering a glimpse into the power of Python for decision-making and repetition in programs.

#### Personal Reflections

Reflecting on Chapter 1, I feel a sense of accomplishment and a growing confidence in my coding abilities. The course's blend of theoretical knowledge and practical application is exactly what I needed. I'm eager to tackle the challenges of Chapter 2, especially the labs, which I anticipate will be more hands-on and directly applicable to my interests in network programmability.

#### Looking Ahead: Chapter 2 - Model Driven Network Programmability

As I close the chapter on Python basics, I look forward with excitement to **Chapter 2: Model Driven Network Programmability**. This next chapter promises a deeper dive into the practical applications of programming in the networking domain, a field I am particularly passionate about.

I aim to approach the upcoming labs with the same enthusiasm and dedication, eager to explore how programming interfaces with networking to drive innovation. The focus on model-driven programmability resonates with my career aspirations, and I am keen to see how these skills will empower me to contribute to the field.

#### Continuous Improvement

My journey through the ETW-MDP course is not just about acquiring new knowledge; it's about applying these skills to solve real problems. I plan to refine my application from Chapter 1, aiming for a more advanced implementation that not only challenges me but also showcases my growing technical prowess.

#### Final Thoughts

This diary serves as a living document of my progress through the ETW-MDP course. Each entry is a step forward in my journey, reflecting on both the triumphs and the trials. I look forward to sharing more of my experiences as I advance through the course, with the hope that my journey can inspire others who embark on this path of discovery and learning.

# Lab Activities:

*Due to personal factor:* Using virtual box for labs was not an option, as it lacking features for Apple Silicon chip. So I decided to work in school lab instead.

## Lab - CLI Automation with Python using netmiko

### Overview:

This lab focuses on automating the Command Line Interface (CLI) with Python using the netmiko library, an essential tool for network administrators looking to simplify network automation tasks through SSH. The lab is structured into four parts, each designed to progressively build your understanding and skills in using netmiko for network automation tasks.

### Required Resources:
- **Access to a router** with the **IOS XE operating system version 16.6 or higher.**
- Internet access.
- A Python 3.x environment.

![[netmiko2.png]]
Figure 1: netmiko connection

Despite having some troubles at the beginning with the basic setup, I have managed to make ssh connection to the router using netmiko and sending commands along with it.

![[netmiko2.png]]
Figure 2: sending commands

Here is server after I sent commands to create Loopback interface and retrieve interface informations.

### Summary:

This part is simple and contained concepts that I have experienced before. However, it is still a good way to learn making requests locally to the server using Python library netmiko.

## 