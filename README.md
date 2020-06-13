# SFIA-2

# bookmovie_app
## LINKS
Presentation : https://onedrive.live.com/edit.aspx?resid=67C6B66CC3D9FFE8!116&cid=fe9c2097-c10b-49ee-bb65-5c554db87130&ithint=file%2cpptx&wdOrigin=OFFICECOM-WEB.MAIN.MRU

Risk Assessment : https://onedrive.live.com/edit.aspx?resid=67C6B66CC3D9FFE8!105&cid=11e27e3c-647a-48fc-92a2-dde06427a580&ithint=file%2cxlsx&wdOrigin=OFFICECOM-WEB.MAIN.MRU

Trello : https://trello.com/b/jzxsxgkl/movie-and-book-app

## Content
* [Brief](#brief)
* [Methods](#methods)
* [Architecture](#architecture)
* [CI Pipeline](#ci-pipeline)
* [Tracking my Project](#tracking-my-project)
* [Risk Assessment ](#risk-assessment)
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


## Tracking my Project
the link for my Trello can be found at : https://trello.com/b/jzxsxgkl/movie-and-book-app

![trello picture](https://user-images.githubusercontent.com/64255340/82814253-b0faea00-9e8e-11ea-9559-fe6f8b70f04e.png)

This Trello is designed to be read and interpreted from left to right with different categorising relating to different parts of the projects as explained below. 

#### Things to do (Beck-end) 
 

This reflects the tasks relating to the logical parts of the app and the code required to complete it. Namely, I would need to construct code allowing users to add a movie or a book as well as code to allow users to update or delete items as they see fit. 

#### Things to do (Front-end) 

This refers to the websites and perhaps the design of it which will need to be completed in Flask. 

#### Things to do (UCD & Database & Planning) 

This category refers to tasks which are non-coding related are ideally based on analysis on risks, documentation of the process, creation of user stories and etc.  

#### Things to do(Testing) 

This category refers to testing of both the front-end and back-end of the project. The beck-end specifically will be tested using pytest. Altogether, there will need to be a high-test coverage and evidence of this shown. 

#### Doing 
This signifies the tasks which I am currently doing. 
#### Done 
This refers to tasks which are completed. 

## Risk Assessment 
The link for the risk assessment can be found - https://onedrive.live.com/edit.aspx?resid=67C6B66CC3D9FFE8!105&cid=1371f661-24ed-4557-b5e7-a18b1901bf6b&ithint=file%2cxlsx&wdOrigin=OFFICECOM-WEB.MAIN.MRU 

It is also shown below: -
![riskassessment1](https://user-images.githubusercontent.com/64255340/82815927-1c928680-9e92-11ea-8e1f-a8543b0e1a17.png)

![riskassessment2](https://user-images.githubusercontent.com/64255340/82815949-25835800-9e92-11ea-9f84-97ec6a79898e.png)

## Testing
![coveragereport](https://user-images.githubusercontent.com/64255340/82816159-8b6fdf80-9e92-11ea-9dca-739e752fadd9.png)

Pytest is a powerful tool used to test the functionality of code. There is a saying “an untested code is a broken code”. Although this may not necessarily be true, it does cause the belief that without tested code, there is no guarantee that the application created will continue to work when it is transferred from development environment to the production environment. Hence it is important that a high-test coverage is achieved. 

Reason for this is that, it will first expose any errors in the code immediately and will also provide confidence that would allow developers to continue adding features without having to waste time and revisit previous written code that was perceived to be working. 

In my own code, I achieved 99% coverage although my initial aim was to achieve 100% aim however, I was unable to trigger the code which would cause an automatic error to display upon the user pressing the delete button on the app without entering information. 

For my own app, I wrote 23 different tests. 

## Web application display of the app 
![DeleteMovie](https://user-images.githubusercontent.com/64255340/82816985-0c7ba680-9e94-11ea-8d98-2fe7bfa7ef66.png)

This is the Delete Page of the side allowing an individual to enter a Book name into the form and if the book placed is within the database, they are given the ability to delete the book from the list. Upon pressing that button, they would be directed to the Book page where they would be able to see that indeed the Book has been removed from the database.  

![Bookpage](https://user-images.githubusercontent.com/64255340/82817031-25845780-9e94-11ea-8761-fa01e9adaff1.png)

This page host all the books that have been added to the database. In this, only the book ID, Book name, authors  name and the Genre will be displayed here. 

![moviepage](https://user-images.githubusercontent.com/64255340/82817063-3634cd80-9e94-11ea-9e06-c51c68520e74.png)
This is the same format for the movie page also where all the movies added will be displayed upon this page.  

![addbook](https://user-images.githubusercontent.com/64255340/82817109-49e03400-9e94-11ea-8e24-6a8d2b79850f.png)
In this page, an individual is able to add books and can only do so by filling in all the given forms which upon completion, they would then be redirected to the Book Page, where they can see their input data has successfully been added to the database.  

![addmovie](https://user-images.githubusercontent.com/64255340/82817140-5b294080-9e94-11ea-9a3f-87f5ff11a67c.png)

This page allows the user to enter a movie and its details which will be saved unto the database. If the movie is made based upon a movie, they can go to the book section and add it according to the books ID and upon submission, there would be a relationship created between the book and the movie. Deletion of this book or movie would cause the complete removal of the added information.

![deletemovie2](https://user-images.githubusercontent.com/64255340/82817203-785e0f00-9e94-11ea-9417-5899e625406a.png)
This page is similar to the delete Book page however it differs in that It will allow the user to delete the movie. 

![update](https://user-images.githubusercontent.com/64255340/82817251-90359300-9e94-11ea-9644-4254313e29eb.png)
This page allows the user to update items in the database. Hence when they enter the Book name, the system will search the database for the book name entered. If the Book can be found within the database, then all the other entered items in the remaining forms will be updated for the book name in question. 


## Issues with Application 

* An issue with the app at the moment is that, you can add the same movie or Books more than once. 

* Another issue is that when you go to update a book, if the book name is not known in the database, the application simply reloads but does not necessarily provide a reason why the page has not redirected to the book page. 

 

## Improvements 

* The Design of the site is the first thing I want to improve. Given that this is an app for Books and Movies, there should be pictures of books and movies to encourage the user to use the site. 

* Furthermore, upon someone adding a movie or book, they should also have the option of attaching a picture alongside or in fact, an algorithm which fetches the picture based upon the name of the book or movie. 

* Another improvement is allowing users to have a personalised account on the app. 

* Another improvement is the incorporate either a selling or a renting function whereby users can sell movies or books to other users within the page.  

* Another improvement is allowing a voting system on the books or movies that individuals will add to the page. 

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





 
 
 
 
 
 
 
