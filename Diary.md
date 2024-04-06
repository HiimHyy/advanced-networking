# Background Check

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

# Course overview

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

##### Highlights

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

# Lab Activities

_Due to personal factor:_ Using virtual box for labs was not an option, as it lacking features for Apple Silicon chip. So I decided to work in school lab instead.

## Lab - CLI Automation with Python using netmiko

### Overview

This lab focuses on automating the Command Line Interface (CLI) with Python using the netmiko library, an essential tool for network administrators looking to simplify network automation tasks through SSH. The lab is structured into four parts, each designed to progressively build your understanding and skills in using netmiko for network automation tasks.

### Required Resources

- **Access to a router** with the **IOS XE operating system version 16.6 or higher.**
- Internet access.
- A Python 3.x environment.

![netmiko](/images/netmiko.png)
Figure 1: netmiko connection

Despite having some troubles at the beginning with the basic setup, I have managed to make ssh connection to the router using netmiko and sending commands along with it.

![netmiko2](/images/netmiko2.png)
Figure 2: sending commands

Here is server after I sent commands to create Loopback interface and retrieve interface informations.

### Summary

This part is simple and contained concepts that I have experienced before. However, it is still a good way to learn making requests locally to the server using Python library netmiko.

## Lab - Explore YANG Models Using the pyang Tool

### Overview

Learn how to use the open source pyang tool to transform YANG data models from files
using the YANG language, into a much more easily human readable format. Using the “tree” view
transformation.

![pyang](/images/pyang.png)
Figure 3: pyang tool

![pyang2](/images/pyang2.png)
Figure 4: yang models of cisco-ios-xe-cdp

## Lab - RESTCONF with Postman

### Overview

Interact with RESTCONF interface using Postman application to retrieve the device's configuration, update and create new interfaces and retrieve operation data.

### Required Resources

- Postman.
- Access to a router with the IOS XE operating system version 16.6 or higher.

![postman](/images/postman.png)
Figure 5: Postman request

![postman2](/images/postman2.png)
Figure 6: Postman response

![postman3](/images/postman3.png)
Figure 7: Postman response with device configuration

![postman4](/images/postman4.png)
Figure 8: New interface created

![postman5](/images/postman5.png)
Figure 9: Make changes to the interface

### Summary

By using Postman, I was able to interact with the RESTCONF interface of the router, retrieve the device's configuration, create new interfaces, and update existing ones. This lab provided a hands-on experience with RESTCONF, reinforcing the concepts learned in the course.

## Lab - NETCONF with Python

### Overview

Following up the previous lab activity, this lab will focus on how to execute the RESTCONF API calls using Python scripts.

### Required Resources

- Python 3.x environment.
- Access to a router with the IOS XE operating system version 16.6 or higher.

![python](/images/python.png)
Figure 10: Python script for NETCONF without formatting

![python2](/images/python2.png)
Figure 11: Python script output with formatting

### Summary

This lab activity provided a practical application of interacting with the NETCONF interface using Python scripts. By executing RESTCONF API calls programmatically, I was able to retrieve device information and configurations, demonstrating the power of automation in network management.

## Lab - raw NETCONF

### Overview

This lab focuses on how to verify that the NETCONF service is running on the device by directly connecting to its port using an SSH client. After that, we will send raw NETCONF Remote Procedure Calls (RPCs) to the device to retrieve information encoded in XML format.

### Required Resources

- Access to a router with the IOS XE operating system version 16.6 or higher.
- An SSH client (e.g., PuTTY).

![netconf](/images/netconf.png)
Figure 12: raw NETCONF

### Summary

For this lab, I used PuTTY to establish an SSH connection to the router and sent raw NETCONF RPCs to retrieve device information. This hands-on activity provided a deeper understanding of the NETCONF protocol and its interaction with network devices.

## Lab - NETCONF w/Python: List Capabilities

### Overview

This lab will focus on how to use the ncclient Python module to easily interact with network devices using NETCONF. And identify which YANG models are supported by the device.

### Required Resources

- Python 3.x environment.
- Access to a router with the IOS XE operating system version 16.6 or higher.

![netconfpython](/images/netconfpython.png)
Figure 13: NETCONF w/Python

### Summary

From this lab, I learned how to use the ncclient Python module to interact with network devices using NETCONF. By listing the capabilities supported by the device, I gained insights into the YANG models available for configuration and management.

## Lab - NETCONF w/Python: Device Configuration

### Overview

This lab focus on how to use the NETCONF ncclient to retrieve the device's configuration, update and create a new interface configuration. And why the transactional support of NETCONF is important for getting consistent network chnages.

### Required Resources

- Python 3.x environment.
- Access to a router with the IOS XE operating system version 16.6 or higher.

![device_configuration](/images/device_configuration.png)
Figure 14: Device Configuration without formatting

![device_configuration2](/images/device_configuration2.png)
Figure 15: Device Configuration with formatting

![device_configuration3](/images/device_configuration3.png)
Figure 16: New interface created

### Summary

This lab activity demonstrated how to use the NETCONF ncclient to retrieve device configurations, create new interfaces, and update existing configurations. The transactional support of NETCONF ensures consistent network changes, making it a powerful tool for network automation and management.

## Lab - NETCONF w/Python: Get Operational Data

### Overview

This lab will focus on how to use the NETCONF ncclient to retrieve operational data from the device.

### Required Resources

- Python 3.x environment.
- Access to a router with the IOS XE operating system version 16.6 or higher.

![get_data](/images/get_data.png)
Figure 17: Get Operational Data

### Summary

By using the NETCONF ncclient, I was able to retrieve operational data from the device, gaining insights into the device's current state and performance. This lab activity showcased the power of NETCONF for collecting real-time data and monitoring network operations.

# Reflection

After finishing all the labs, I have gained a deeper understanding of network programmability concepts and tools. The hands-on experience with netmiko, pyang, Postman, and Python scripts for NETCONF interactions has been invaluable in reinforcing the theoretical knowledge from the course.
