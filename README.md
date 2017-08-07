# Safaricom_social_tracker_app
Socio-Tracker

This is an application that uses machine-learning to monitor people's attitude in social media (twitter) towards a product or topic in debate as positive or negative. Once logged in, users are provided with an interface to enter a "key word" or "search topic". The "key word" or "key topic" is searched through twitter(dev.twitter) and then processed by the backend code. The results are then rendered in a graph.

SOFTWARE ARCHITECTURAL CONSIDERATIONS:-

Handling over 1M users - Scalability is one of the most important aspect in design of modern software architectures. Below are some techniques to ensure that the system is scalable:- a. Three tier approach that involves:- * The client tier - responsible for interacting with the user via a Graphical User Interface (GUI) and submitting requests via the network to the mid tier. Use of Html and Javascript charts to submit requests and render results respecively. * The mid-tier - responsible for gathering requests from clients and executing transactions against the data tier. Use of JavaScript Object Notation (JSON). * The data tier - responsible for physical storage and manipulation of the information represented by application queries and the responses to those queries. Use of a relational database engine (e.g MYSQL) b. Service Oriented approach:- This involves decoupling of functionality; grouping of components into "areas of concern". Different functionalities/contexts interact with each other through abstract interface. In this design the different components are contextualized through pickling (creating pickles).

Concurrency:- This is where several computations are executed during overlapping time periods. In this case use of thread-safe structures is adopted.

High I/O:- In this project, word tokenization and speech tagging is utilized. This involves breaking of sentences into words and classifying the according to their respective parts of speech; only adjectives are used to determine the sentiment/attitude.

Utilization of front end and Backend. Front end - Html and Javascript have been used. This ensures that the site comes up correctly in different browsers (cross-browser), different operating systems (cross-platform) and different devices (cross-device). Backend - Python is used in the backend. As different tasks are contextualized, most variables are local variables. python accesses local variables more efficiently than global variables. Also use of looping structures to loop over a sequence of words in sentences. Python was also preferred as its machine learning libraries and community community is more developed/wide.

Adoption of asynchronous communication:- The sending activity forwards its information regardless of whether the receiver is ready to receive it or not. The receiver buffers inputs if not in a position to process them for future processing.
