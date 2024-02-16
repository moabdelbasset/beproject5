# TaskWave

Please note, this README is for backend database of a full stack application. This API provides a backend database to allow all [this](#site-goals) functionality. You can view the [API here](https://beproject5-5d5ddb867f18.herokuapp.com/). To view it in a nicer format install a JSON extension like [this one](https://chromewebstore.google.com/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc) if you're using Chrome.


For details on front-end please visit this link: [FRONT-END REPO](https://github.com/moabdelbasset/feproject5), and if you click [HERE](https://feproject5-c5d5d2304ed4.herokuapp.com/), you can see live full stack deployed live website.

## Table of Contents

- [TaskWave](#taskwave)
  - [Table of Contents](#table-of-contents)
- [User Experience Design](#user-experience-design)
  - [The Strategy Plane](#the-strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Epics](#epics)
      - [User Stories](#user-stories)
  - [The Structure Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The Skeleton Plane](#the-skeleton-plane)
    - [Database Design](#database-design)
- [Technologies](#technologies)
  - [Tools and Technologies](#tools-and-technologies)
  - [Imports](#imports)
    - [Installed Packages](#installed-packages)
- [Testing](#testing)
  - [Validator Testing](#validator-testing)
    - [Python](#python)
  - [Manual Testing](#manual-testing)
    - [Functional Testing](#functional-testing)
      - [Negative Testing](#negative-testing)
  - [Automatic Testing](#automatic-testing)
    - [Unit Tests](#unit-tests)
- [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Deploying in Heroku](#deploying-in-heroku)
    - [Cloning the Repository](#cloning-the-repository)
    - [Forking](#forking)
- [Credits](#credits)


# User Experience Design

## The Strategy Plane

### Site Goals

TaskWave is a productivity application developed for users to be able to organize their tasks and help them achieve thier goals. Anyone can register, sign in and start creating your tasks. The website is designed to be user friendly and make your experience smooth and easy. Users can contact the developer and ask questions incase if they are indoubt or they face any problems. Users can also assign the task a priority, status, and due date which gives the user a better sense of urgence to his tasks and increase their productivity. Users can also edit their tasks and update the task field according for how much they accomplished. In the home page users can check their progress of their tasks in a progress bar to better visualize their progress. Also, They can get an alarm or warning if the task due is coming soon or if it is passed.

### Agile Planning

The project was developed using agile methodology. Small features have been assigned to 6 EPICS.
Labels have been used to mark which features the project : 'must have', 'should have', 'could have'. This was done so that I create a MVP in the time I have and only focus on the 'should have's' or 'could have's' if time allows. 
Each user story was closed if all acceptance criteria have been met.

Project board has been used to help me with the process [PROJECT BOARD-link](https://github.com/users/AsiaWi/projects/5/views/1?layout=board)

#### Epics

- 1-Project setup:
   This was a first task without it I wouldn't be able to continue with any of the project features so it was necessary to set up a basic structure of the project following the user stories included in this Epic.
- 2-Authentication/navigation:
   This milestone was needed to allow users to actually use the page so that the page is interactive
- 3-Profile:
   Includes all features enabling the CRUD functionality for the user
- 4-Contact page:
   This improves users journey throughout the page and makes it a smooth experience for everyone.
- 5-Tasks Page:
   Includes all features enabling the CRUD functionality for the user
- 6-Documentation and deployment: 
   Absolutely necessary step to make sure the page is deployed with no erros and allows anyone access to all features.Needed to document the project

#### User Stories

 Each EPIC contains user stories allowing me to build up the project with small features:

- EPIC 1- Project setup
  - `As a DEVELOPER I need to SET UP THE PROJECT so that i CAN BUILD THE PAGE`
  - `As a DEVELOPER I need to CONNECT THE PROJECT TO CLOUD TO STORE IMAGES so that USERS CAN UPLOAD IMAGES`
- EPIC 2-Authentication/navigation:
  - `As a USER I can REGISTER AND SIGN IN so that I CAN ACCESS CONTENT WHICH REQUIRES TO BE AUTHORISED`
- EPIC 3-Profile:
  - `As a LOGGED IN USER I can view my profile`
  - `As a LOGGED IN USER I can edit my profile`
- EPIC 4-Contact Page:
  - `As a USER I can contact the developer in case if any issues or questions I have`
- EPIC 5-Tasks Page:
  - `As a LOGGED IN USER I can view my tasks`
  - `As a LOGGED IN USER I can edit my tasks`
  - `As a LOGGED IN USER I can delete my tasks`
- EPIC 6-Documentation and deployment:
  - `As a DEVELOPER I need to CREATE README FILE so that I CAN DOCUMENT THE PROCESS OF CREATING THE APPLICATION`
  - `As a DEVELOPER I need to deploy both projects and link them together so that USERS CAN USE FULL STACK WEBSITE`

## The Structure Plane

### Features

#### Homepage

You will see a welcome message, please see the features below where links to all the existing features will be provided

![API-HOME](https://res.cloudinary.com/dxiyxikz7/image/upload/v1708022141/media/images/a9efc7f8-9747-4ba1-8c72-54ec549cdc64.png)

All features have been implemented with user stories in mind 

#### Profile

`As a LOGGED IN USER I can view my profile`

`As a LOGGED IN USER I can edit my profile`

The advert list view can be accessed here: https://beproject5-5d5ddb867f18.herokuapp.com/profiles/<id>/

    -Endpoint ``/profiles/init:pk``
    -Methods used:
     `GET`  used to list view profile
     `POST` used to create a profile

![Profile_VIEW](https://res.cloudinary.com/dxiyxikz7/image/upload/v1708022857/media/images/94886513-057b-4695-8600-29e9d9922011.png)

Page can be accessed as logged in user and if you logged in as admin during the development phase you can list all the added users

To see fields included in the model see [Database Design](#database-design) 

Additional fields added with the help of serializer to JSON data:

 - is_owner

### Features left to implement

In the future I would like to add additional model for potential buyers and seller to communicate privately so that they could exchange private details there and arrange further details of transaction. I initially added private message to Offers model however as I wanted to make everything but the message available to all users based on `isAuthorisedOrReadOnly` permissions I decided to remove the message. 

## The Skeleton Plane

### Database design

![entity_relationship_diagram](https://res.cloudinary.com/dxiyxikz7/image/upload/v1708024417/media/images/62aa9eba-70fe-45bd-a4a3-d7fe8a8ab6a9.png)

- The ER Diagram has been generated with DBeaver. 
- The diagram shows relationships between models
  - auth_user: 
    - Represents the User table typically provided by Django's authentication system.
    - Fields include id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, and date_joined.
  - account_emailaddress:
    - Linked to auth_user by user_id.
    - Contains fields such as `id`, `email`, `verified`, `primary`, and `user_id`.
  - account_emailconfirmation:
    - Linked to `account_emailaddress` by `email_address_id`.
    - Includes `id`, `created`, `sent`, and `key`.
  - profiles_profile:
    - Connected to `auth_user` by `owner_id`.
    - Represents user profiles with fields such as `id`, `name`, `image`, and `owner_id`. 
  - tasks_task:
    - Contains task-related data with fields like `id`, `title`, `description`, `status`, `priority`, `due_date`, `created_at`, `updated_at`, and `assigned_to_id`.
    - It's linked to `profiles_profile` via `assigned_to_id`, indicating which user the task is assigned to.
  - contacts_contact:
    - This is a table for contact inquiries or messages with fields such as `id`, `name`, `email`, `subject`, `message`, and `created_at`.  


## Technologies

### Tools and technologies

* Visual Studio Code - used to develop the website
* Github - used to host source code and deploy on Github Pages
* Git- used to commit and push code 
* Python - used as the main language to code the logic of the page
* Django==4.2.8 - framework used
* djangorestframework==3.14.0 - framework used
* Heroku - to deploy the app 
* [dbeaver](https://dbeaver.com/) - used to generate the ER Diagram

### Imports

#### Installed packages

* asgiref==3.7.2
* cloudinary==1.38.0
* dj-database-url==0.5.0
* dj-rest-auth==2.1.9
* Django==3.2.23
* django-allauth==0.44.0
* django-cloudinary-storage==0.3.0
* django-cors-headers==4.3.1
* django-filter==23.5
* djangorestframework==3.14.0
* djangorestframework-simplejwt==5.3.1
* gunicorn==21.2.0
* oauthlib==3.2.2
* pillow==10.2.0
* psycopg2==2.9.9
* PyJWT==2.8.0
* python-decouple==3.8
* python3-openid==3.2.0
* pytz==2023.3.post1
* requests-oauthlib==1.3.1
* sqlparse==0.4.4

## Testing

### Validator Testing

#### Python

No errors shows when passing each file through [CI Python Linter](https://pep8ci.herokuapp.com/)

Each python file in this repo has been run through and each file received the same success message:

![python_validator_check](https://res.cloudinary.com/dxiyxikz7/image/upload/v1708025534/media/images/2d5c6b4f-e6ed-495f-8043-3f351b9687fd.png)

### Manual Testing

#### Functional Testing
 All functions have been manually tested to make sure each function works as intended and only for users as intended. Testing of the entire full stack application can be found within [FRONT-END REPO](https://github.com/moabdelbasset/feproject5)

##### Negative Testing
 All functions have been tested to make sure no functions are available to unauthorised users etc. This was done throughout the entire development process. Full application testing can be found on [FRONT-END REPO](https://github.com/moabdelbasset/feproject5)

### Automatic Testing

#### Unit Testing

Unit tests have been performed in frontend


## Deployment

### Version Control

* Git 
    Code has been pushed with git commands to remote repository on Github with commands:

   `` git add .`` - to add files ready to commit

   ``git commit -m "message"`` - to commit the code to local 
    repository ready to be pushed

   ``git push`` - final command used to push commited code to remote repo on Github

### Deploying in Heroku 

* The project has been deployed on Heroku as follows:
     * Use: ``pip freeze > requirements.txt`` to add external libraries to deployed app.
     * Create Heroku account ( step by step guide [here](https://coding-boot-camp.github.io/full-stack/heroku/deploy-with-heroku-and-mysql))
     * In the top right, click 'New'
     * Click 'Create new app'
     * Give your app a name and select your region from drop down 
     * Click 'Create new app' 
     * Go to 'settings' tab, it's important you do it before deployment
     * Scroll down to 'config vars' section and key:
        - ALLOWED_HOST : add url to your heroku app link
        - CLIENT_ORIGIN : frontend heroku url which will be making requests to this API 
        - CLIENT_ORIGIN_DEV: local front-end url
        - CLOUDINARY_URL: 'API key to your cloudinary account'
        - DATABASE_URL : 'URL from your database account'
        - SECRET_KEY: 'Generate your own secret key'
        - DISABLE_COLLECTSTATIC: set to '1'
     * Scroll down to 'Buildpacks' section
     * Click 'Add buildpack'
     * Add Python as first dependency and select 'Save changes'
     * Add node.js as a second dependency and save again
     (This is settings section done)
     * Select 'Deploy' tab at the top
     * Select ' Github' from 'Deployment method'
     * type the name of how you called project in Github and click 'search'
     * Scroll down and select manual deployment method
     * Auto method has also been selected to allow the project to update every time i push the code from Gitpod
     * You can now click to view the app ready and running

### CLONING THE REPOSITORY

1. On Github navigate to repository
2. Click "Code" a green button shown right above the file list
3. Copy the URL of the repo using HTTPS, SSH OR Github CLI
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory
6. Type git clone, and then paste the URL you copied earlier
7. Press enter to create local Clone

For more details on how to clone the remote repo in order to create a local copy for own use, please click [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)


### FORKING

1. On Github navigate to repository
2. click "Fork" located towards the top right corner
3. Select "owner" for the forked repo, from the dropdown menu under "owner" Under "Owner"
4. It will create forked repo under the same name as orinial by default but you can type a name in "Repository name" or add a description in "Description" box.
5. Click "Create fork" !

Forking allows you to make any changes without affecting original project. You can send the suggestions over by submitting pull request. Project owner can review the pull request before accepting the suggestions and merging them.

For more details on how to fork the repo, in order to for example suggest any changes to the project you can click [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo) 

When you have fork to a repository you don't have access to files locally on your device, for this you will need to clone the forked repo.

## Credits

- Code Insitute's DRF walkthrough
- My mentor [Daisy Mc Girr](https://github.com/Daisy-McG) for helping me during the project. Her insights were really helpfull along all the projects and I learned from her alot.
- All the links below to help me with creating average rating for list and detail views:
    - [When()](https://docs.djangoproject.com/en/4.2/ref/models/conditional-expressions/)
    - [F()](https://docs.djangoproject.com/en/5.0/ref/models/expressions/)
    - [Stack overflow](https://stackoverflow.com/questions/68953258/%20how-to-calculate-average-of-some-field-in-django-models-and-send-it-to-rest-api) 
    - [django fun](https://django.fun/qa/16172/)
