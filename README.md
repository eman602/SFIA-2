# SFIA-2

# Baby Name Generator
## LINKS
Trello : https://trello.com/b/iPcYe9QR/baby-name-generator-app

## Content
* [Brief](#brief)
* [Methods](#methods)
* [Architecture](#architecture)
* [CI Pipeline](#ci-pipeline)
* [MoSCoW Analysis](#moscow-analysis)
* [Tracking my Project](#tracking-my-project)
* [Risk Assessment ](#risk-assessment)
* [Deployment ](#deployment)
* [Testing](#testing)
* [Web application display of the app](#web-application-display-of-the-app)
* [Issues with Application](#issues-with-application)
* [Improvements](#improvements)
* [Licensing](#licensing)
* [Acknowledgments](#acknowledgments)
* [Contributors](#contributors)
* [Author](#author)

## Brief
The aim of the app was to create an app which has its functions based upon 4 microservices which would be deployed using specific DevOps tools. The Architecture of the site will be micro-services orientated which must work together.
In more detail:-
* Service 1 will have the ability to use Jinja2 templates which will need to interact with my application, this first service will also be required to speak to the remaining 3 services and the information received will be persisted into an SQL database. In relation to my app, I decided to create random baby name generator hence Service 1 would ideally detail the babies name that has been generated and persist it into an SQL database. 

* Service 2 for my app will generate the first name of the name that will be displayed hence from a list of names, a random number will be selected pertaining to the index of a name in the list which will then be passed on to service 4. 

* Likewise, Service 3 will have surnames in a list and a random number generated pertaining to its index. The chosen number will then be sent to Service 4.

* The last Service_4 will create a full name made up from the results of both service 2 and 3. This will the be the Object created. The Information will be sent to Service 1 and that will add it to a database known as baby names. 
Naturally, this project is designed in order that certain DevOps tools can be used i.e. Docker, Jenkins, Ansible and Nginx. 

All these services would be deployed using Jenkins as the open-source server for continuation integration. Docker would be used for containerisation specifically docker swarm. The necessary environments will be implemented using ansible and more information of these will be shown further in this report.

 ## Methods

* The source code for creating the 4 different microservices will be completed within Visual studio Code due to its ease of use.

* The use of SQL will be used in order to persist the data(full name) created by all my microservices. 

* The Version Control System used will be GitHub and a webhook connection will be established with Jenkins in order that all features 
pushed to GitHub will be triggered and automatically built by Jenkins and deployed unto using my IP address.

* The tools for Containerisation will be docker. With Docker you can create a dockerfile for every container of your site. The options for Docker is that you can build and push your docker images to a local repository or to DockerHub which is the approach I will be going for in order that any updates or new features can be sent to DockerHub, allowing Jenkins to pull down these images and automatically build.

* I will also use Nginx which will service as a reverse-proxy. It will be implemented to listen for traffic on a given port and redirect this traffic to a chosen port. It will also act as a load balancer.

* I will use Ansible in order that I can create a master-node and a worker-node. This will allow me to successful use Jenkins to implement a rolling update of a new feature to my site. By doing so, the website will remain running whilst this new feature of being built allowing for a seamless transition for the users. 


## Architecture
#### Database Structure

##### Current
![sqltableplan](https://user-images.githubusercontent.com/64255340/84569859-6bd92200-ad81-11ea-8f29-9d09eeac2b04.png)

This image is currently what the structure of the database is built on as as shown, we have the primary key being the id of each name which will be auto incrementing for every name that is generated and persisted into the database. 

#### User Case
![userstory](https://user-images.githubusercontent.com/64255340/84569894-aba00980-ad81-11ea-8fb0-8fb22066ca69.png)

This is an outline description of what is possible for the user to be able to do and also how the computer will respond to their request. Within the app, the users request will be recognised by the server through either the POST Method or the GET method.
In more details, the user will be to access the site and simply look at names that have already been generated which is made possible by a code written that will retrieve the information and simply display that on the website. 
On top of this, the user will be able to click on a generate buttom on the screen which simply refreshes the site and as it does so, it also display a random combination of names on the site and persist this on to the SQL database. 


## CI Pipeline
![CIpipeline](https://user-images.githubusercontent.com/64255340/84571227-ceceb700-ad89-11ea-8b87-ddc03e968221.png)

The continous integration pipeline begins at the  python level in which the source code is constructed in VS code and tested using python3 app.py. After the code successfully worked in the development server, the code is then pushed up to github under the repository name bookmovie_app. Currently there are 3 branches being used and the most updated one being the testing branch. This branch has a connection through webHook with hence any changes made here will be picked up by the CI tool Jenkins and automatically configured and built. 

In my CI pipeline, I planned to have Jenkins run my automatic test as shown however, in reality, all code was tested using unit testing in pytest before the code was pushed up to git hub and integrated into the app. Jenkins will install the flask and import all the necessary modules. 

Code is checked by Jenkins and if it is sufficient, it will then be built without an error message being sent. 
At the very beginning of the process, all the required work are put on Trello and the required work is recieved from Trello and once is it completed, it is then updated in Trello and another piece of work is taken.

The Jenkins project is built using a pipeline as opposed to a freestyle project, hence in order to keep files organised, a Jenkinsfile is utilised which essentially allows Jenkins to build specific parts of the application using environments that are prescribed to it. 
An example is having it access different files to install docker and then set up ansible as well as having different files in different sections which the docker-compose file can launch. 

Docker in the CI pipeline is where images of my containers are pushed to. Hence to clarify, my four microservices will each serve as a container and an image of each will be produced and pushed to my designated repository in DockerHub. This provides Jenkins the ability to the access my DockerHub as it is open source, and then pull down the image and run that image as part of the prerequisite to build my application. 

There may also be instruction for Jenkins to update the docker images in my docker repository hence that can also be executed. 
Ansible is also used in order to allow an environment to be initialised in the worker-node. It is also used to determine which of my nodes will play the role as the master node or the worker node. 
Finally, the application is run entirely using Nginx. It is designed to listen on port 80 and redirect traffic to port 5000. 


## MoSCoW Analysis

#### Must have Have
 * You are required to create a micro-service orientated architecture for your application, this application must be composed of at least 4 services that work together.
 
* Service 1 The core service – this will render the Jinja2 templates you need to interact with my application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.

* Service 2 + 3
These will both generate a random “Object”, this object can be whatever l like as we encourage creativity in this project.


* Service #4 This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.  Please see below for an example of how this logic can look.

* Kanban Board: Asana or an equivalent Kanban Board 

* I will also need to demonstrate the working CI Pipeline that you have been able to build by rolling out updates to the system, without interrupting the user experience.  

#### Should Have
* Web hooks should be used
* Docker swarm is used over compose to enable deployment to multiple nodes.
* Documentation includes progression throughout the project.

#### Could Have
* A fully functioning CRUD application accessible through Service 1.
* Testing completed for front end of my application. 


## Tracking my Project
the link for my Trello can be found at : https://trello.com/b/iPcYe9QR/baby-name-generator-app

![trelloboard](https://user-images.githubusercontent.com/64255340/84579580-c2b51a80-adc6-11ea-947e-bd2cdf9ffd3e.png)

This Trello is designed to be read and interpreted from left to right with different categorising relating to different parts of the projects as explained below. 

#### Front End task

This reflects the tasks relating to the logical parts of the app and the code required to complete it. Namely, I would need to construct code allowing users to access the site and generate a random name from it. 

#### Back End
This refers to the logic my of site and what must take place in order for the outcome on the front end to occutr

#### Documentation

This category refers to tasks which are non-coding related are ideally based on analysis on risks, documentation of the process, creation of user stories and etc.  

#### Testing task

This category refers to testing of both the front-end and back-end of the project. The beck-end specifically will be tested using pytest. Altogether, there will need to be a high-test coverage and evidence of this shown. 

#### In progress 
This signifies the tasks which I am currently doing. 
#### Completed 
This refers to tasks which are completed. 

## Risk Assessment 

It is also shown below: -
![risk1](https://user-images.githubusercontent.com/64255340/84580465-365b2580-adcf-11ea-8ff8-ad98f1f44622.png)

![risk2](https://user-images.githubusercontent.com/64255340/84580472-4115ba80-adcf-11ea-828c-ab186b7606b8.png)

![matrix](https://user-images.githubusercontent.com/64255340/84592418-7f49c300-ae3d-11ea-836c-a23df7fe6406.jpg)

This matrix show for the large part of my project, most of my risks  likelihood aswell the the impact(consequences) of it happening usually fell below the moderate(orange) and low(green) areas. The risk that I had to take care of mostly was that concerning exposing certain environment variables partaining to either my database url or the secret keys. 
Upon reflection of the risk matrix in concern with my risk assessment I understood that I do not need to admend my risks as I related back to them throughout the project to ensure that the mitigation methods that I proposed were being adhered to. 

## Deployment

![buildpipeline](https://user-images.githubusercontent.com/64255340/84593816-187cd780-ae46-11ea-8660-43533b3147e4.png)
The deployment of my project is as shown below. With the left part showing some of the build history. As shown, as of 12/06/2020, I had implemented 91 total builds with each build essentially fulfulling a different purpose.
The builds below 80 where for testing the visual aspect of the app and making sure they worked thoroughly and in situation where they did not, implementing the necessary changes and re-running those test again. 

In this section I will outline the tools I used and the reasons behind using those tools as well as a brief justification of why I moved into cloud.

Tools used for deployement: -
* (Jenkins)
Jenkins in definition is an open source automation tool which was written in java for the purpose of fulfilling business continuous integration problem. It allows the users to build and test the software projects continuously hence making it easier for developers to integrate changes to the project and it also allows for users such as myself to obtain a fresh build. Aside from Jenkins, other options available would have been CircleCI, Red Hat and etc however I chose Jenkins not just because it is largely encouraged at QA but because Jenkins is much leaner at allowing for automating process when adding new code all the way through to acceptance testing. This Continuous delivery tool allows for a high level of automation of all steps.  Running Jenkins allows us to continuously check that the code compiles. The only few disadvantages of Jenkins is its initial setup. For my project, I constructed a Jenkins file which details exactly which directory Jenkins can go to execute every code required and build the necessary environment in order to allow the code to run as is required. 

* (Docker)
I also used Docker as one of my deployment tools. Docker is essentially designed to make it easier to create, deploy and run applications using containers. These containers provide developers the ability to package an application with all the required parts such as the modules, libraries and dependencies and then deploy it as one package. This is rather more convenient than doing it through a virtual machine, mostly due to the fact that the length of time required to deploy the application through Docker is massively decreased given that the machine deployed on also has Docker installed. However, in comparison to virtual machines, the necessary environment may not always be present and if the user is using a Linux or a mac, these can also bring up potential issues during its deployment. Apart from it being encourages in QA for the use of Docker, my reason for using it is because it eases the pain of debugging environments. Docker gives the ability to isolate and eliminate environment issues without necessarily needing to know how my worker-node is setup. 

* (Ansible)
Ansible is also another tool for deployment I used an its function was to serve as an open source IT configuration management, deployment and Orchestration tool. One of the strongest aspects of using ansible is that it allows me to automate complex multi-tier IT application environments. For example, through its automation ability I removes me having to manually install Docker on my worker node to now being able to write a Playbook.yaml file in which the code within would a allow the necessarily environment to be set and additionally add my worker-node as a worker to my docker swarm. 

* (Pytest)
Pytest was used to test my written code especailly for the back-end code of my application. 

* (Nginx)
Nginx is open-source free, high-performance HTTP server and reverse proxy. It is known mostly for its high performance and low resource consumption capabilities. I specifically used it in my project to act as a load balance and as a reverse proxy. Nginx is naturally configured to run on port 80 hence by configuring it to listen for any traffic coming to port 5000 where my project is located and then redirecting it to port 80. Nginx can also increase the safety of the app as it acts as another layers siting between the client and the server.

## Testing
I tried within my project to adhere to some test driven development during my project, especially when I was attending to the code for my microservice 2 and 3. I had test in place to ensure that the random values which would be selected would always be in range.

#### Test coverage for Service 1
![testservice1](https://user-images.githubusercontent.com/64255340/84580981-63f69d80-add4-11ea-9fa6-7072eb5d2821.png)

#### Test coverage for Service 2
![testservice2](https://user-images.githubusercontent.com/64255340/84580987-6f49c900-add4-11ea-9f96-14c3263e6013.png)

#### Test coverage for Service 3
![testservice2](https://user-images.githubusercontent.com/64255340/84580987-6f49c900-add4-11ea-9f96-14c3263e6013.png)

#### Test coverage for Service 4
![testservice4](https://user-images.githubusercontent.com/64255340/84580997-7b358b00-add4-11ea-9749-2b34c79a894e.png)

Pytest is a powerful tool used to test the functionality of code. There is a saying “an untested code is a broken code”. Although this may not necessarily be true, it does cause the belief that without tested code, there is no guarantee that the application created will continue to work when it is transferred from development environment to the production environment. Hence it is important that a high-test coverage is achieved. 

Reason for this is that, it will first expose any errors in the code immediately and will also provide confidence that would allow developers to continue adding features without having to waste time and revisit previous written code that was perceived to be working. 

In my own code, I achieved an average of 87% test coverage although my initial aim was to achieve 100% aim however, 
For my own app, I wrote 4 different tests. 

## Web application display of the app 
![webpage](https://user-images.githubusercontent.com/64255340/84581078-2f371600-add5-11ea-8c6c-abb372a01a86.png)

This is a display of the app. The generate buttom allows for the site to be refreshed and a new name is generated upon which it is then persisted into a database and of course a query of this database is made in order to display the list of names that have already been persisted.

## Issues with Application 

* An issue with the app at the moment is that, if the same name is generated, it is still persisted hence causing duplications.

## Improvements 

* The Design of the site is the first thing I want to improve. Given that this is an app for names, there should be pictures of families. 

* Also making it possible for people to write a name and get feedback on whether the name is appropriate for a child. 

* Another improvement is allowing users to have a personalised account on the app.  

* Another improvement is allowing a voting system on the names that individuals will add to the page. 

## Licensing
Copyright 2020 Emmanuel Agyapong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgements
I will like to express an appreciation to Ben Hesketh, Luke Benson and Syed Ahmed for their constructive suggestions during the development of this project. 

## Contributors 
Emmanuel Agyapong

## Author
Emmanuel Agyapong





 
 
 
 
 
 
 
