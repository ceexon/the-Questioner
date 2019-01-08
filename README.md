# Questioner

The questioner app is a web that allows users who are attendees of a meetup to be able to raise questions they would like to discuss in the meetup. The questions are then voted on by feelow users to determine which has more priority over the others. The question with most votes is deemed as one with a highest priority.

## QUESTIONER API V1

**Badges**

The Related Pivotal tracker board is **[Here](https://www.pivotaltracker.com/n/projects/2235288)**

## What is required

- Python3
- Flask
- Postman
- Pytest
- Git
- Python3 pip

## How to get started

1. Clone the repo

   > `https://github.com/kburudi/the-Questioner/`

2) Checkout delelop branch

   > `git checkout develop`

## First install

1. python3

   > `sudo apt-get install python3`

2. install python3 pip

   > `sudo apt-get install python3-pip`

3. install vitual environment

   > `pip3 install virtualenv`

4. checkout develop branch

   > `git checkout develop`

5. create the virtual environment

   > `virtualenv env`

6. Activate the vitualenv in the parent directory of your **"env"**

   > `source env/bin/activate`

7. Install requirement

   > `pip install requirements.txt`

8. Run the app

   > `python3 run.py`

## Endpoints to use on postman

| Endpoints                                 |               Functions               |
| ----------------------------------------- | :-----------------------------------: |
| POST/api/v1/signup                        |            create new user            |
| POST/api/v1/login                         |        sign in to your account        |
| POST/api/v1/meetup                        |             create meetup             |
| GET/api/v1/meetup                         |            get all meetups            |
| GET/api/v1/meetup/id                      |         get a specific meetup         |
| POST/api/v1/meetup/id/question            |       add question for a meetup       |
| GET/api/v1/meetup/id/question             | view all questions for a given meetup |
| DELETE/api/v1/meetup/id                   |            delete a meetup            |
| POST/api/v1/meetup/id/rsvp                |     respond to meetup invitation      |
| PUT/api/v1/meetup/id/question/id/vote     |     upvote or downvote a question     |
| POST/api/v1/meetup/id/question/id/        |       view a specific question        |
| POST/api/v1/meetup/id/question/id/comment |         comment on a question         |
| GET/api/v1/meetup/id/question/id/comment  |    view all comments on a question    |

## Authors

Trevor Kurland

## Acknowledgements

1. Andela-Workshops
2. Team-mates
