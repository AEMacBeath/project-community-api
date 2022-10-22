# Project Community - API

## Project Description
Project Community is a social media platform designed for users to share safety observation reports. The application is made up of a Django API ([project-community-api](https://project-community-api.herokuapp.com/)) and a React app ([project-community-ci](https://project-community-ci.herokuapp.com)).

## Development
This API was developed as a series of small tasks recorded as [GitHub Issues](https://github.com/AEMacBeath/project-community-api/issues?q=is%3Aissue+is%3Aclosed+sort%3Acreated-asc).

## User Stories
The user stories for this API where written in conjuncion with the React application using [@AEMacBeath's Project Community](https://github.com/users/AEMacBeath/projects/11/views/1) GitHub Project.

The GitHub project is grouped by Milestones broken down into User Stories and Tasks. 

## Models and CRUD breakdown
![model-crud](/documentation/screenshots/model-crud.png)

## Entity Relationship Diagram
![relationship-diagram](/documentation/screenshots/relationship-diagram.png)

## Testing
- Posts app:
    - logged out users can list posts
    - logged in users can create a post
    - logged out users can't create a post
    - logged out users can retrieve a post with a valid id
    - logged out users can't retrieve a post with an invalid id
    - logged in users can update a post they own
    - logged in users can't update a post they don't own

## Deployment
- set the following environment variables:
    - CLIENT_ORIGIN
    - CLOUDINARY_URL
    - DATABASE_URL
    - DISABLE_COLLECTSTATIC
    - SECRET_KEY
- installed the following libraries to handle database connection:
    - psycopg2
	- dj-database-url
- configured dj-rest-auth library for JWTs
- set allowed hosts
- configured CORS:
	- set allowed_origins
- set default renderer to JSON
- added Procfile with release and web commands
- gitignored the env&#46;py file
- generated requirements.txt
- deployed to Heroku
