# Project Community - API

## Project Description
Project Community is a social media platform designed for users to share safety observation reports. The application is made up of a Django API and a React app.

### API
GitHub Repository - [project-community-api](https://github.com/AEMacBeath/project-community-api)<br>
Heroku App - [project-community-api](https://project-community-api.herokuapp.com/)

### React App
GitHub Repository - [project-community-ui](https://github.com/AEMacBeath/project-community-ui)<br>
Heroku App - [project-community-ci](https://project-community-ci.herokuapp.com)


## Development
This API was developed as a series of small tasks recorded as [GitHub Issues](https://github.com/AEMacBeath/project-community-api/issues?q=is%3Aissue+is%3Aclosed+sort%3Acreated-asc).

## User Stories
The user stories for this API where written in conjuncion with the React application using [@AEMacBeath's Project Community](https://github.com/users/AEMacBeath/projects/11/views/1) GitHub Project.

The GitHub project is grouped by Milestones broken down into User Stories and Tasks. 

### API User Stories
| Milestone      | User Story                                                                                                                                 | Task                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| Authentication | Sign up - As a user I can create an account so that I can access all the features.                                                         | Install dj-rest-auth                    |
| Navigation     | Routing - As a user I can I can move between pages quickly so that I can view content without waiting for the page to refresh.             | Add Root Route                          |
| Profiles       | Create Profile - As a user I can create a profile so that I can express myself.                                                            | Start Profiles App                      |
| Profiles       | Create Profile - As a user I can create a profile so that I can express myself.                                                            | Create Profile Model                    |
| Profiles       | Create Profile - As a user I can create a profile so that I can express myself.                                                            | Add Signal to Profile Model             |
| Profiles       | Other User's Profiles - As a user I can view other user's profiles so that I can read their observations.                                  | Create Profiles Serializer              |
| Profiles       | Other User's Profiles - As a user I can view other user's profiles so that I can read their observations.                                  | Create ProfileList View                 |
| Profiles       | Other User's Profiles - As a user I can view other user's profiles so that I can read their observations.                                  | Create ProfileDetail View               |
| Observations   | Create Observation - As a user I can create an observation so that it can be viewed by other users.                                        | Start Observations App                  |
| Observations   | Create Observation - As a user I can create an observation so that it can be viewed by other users.                                        | Create Observation Model                |
| Observations   | View Observation - As a user I can view an observations so that I can read the details.                                                    | Create ObservationDetail View           |
| Observations   | View Observation - As a user I can view an observations so that I can read the details.                                                    | Create Observations Serializer          |
| Observations   | View Observations List - As a user I can view a list of observations so that I can choose which one to read.                               | Create ObservationList View             |
| Observations   | Search - As a user I can search for observations so that I can easily find ones I am interested in.                                        | Refactor Observation Views to Generics  |
| Observations   | Search - As a user I can search for observations so that I can easily find ones I am interested in.                                        | Add Observation Search                  |
| Observations   | View latest Observations - As a user I can view latest observations first so that I can stay up to date with content.                      | Sort ObservationList by created_at date |
| Observations   | User Observations - As a user I can view observations made by a specific user so that I can view their latest observations.                | Add Observation Filter functionality    |
| Comments       | Create Comment - As a user I can create comments on observations so that I can give feedback to other users.                               | Start Comments App                      |
| Comments       | Create Comment - As a user I can create comments on observations so that I can give feedback to other users.                               | Create Comment Model                    |
| Comments       | Create Comment - As a user I can create comments on observations so that I can give feedback to other users.                               | Create Comments Serializer              |
| Comments       | View Comments - As a user I can view comments so that I can see other users feedback.                                                      | Create CommentList View                 |
| Comments       | View Comments - As a user I can view comments so that I can see other users feedback.                                                      | Create CommentDetail View               |
| Likes          | Like and Unlike Observations - As a user I can like / unlike observations and comments so that I can highlight my interest in the content. | Start Likes App                         |
| Likes          | Like and Unlike Observations - As a user I can like / unlike observations and comments so that I can highlight my interest in the content. | Create Like Model                       |
| Likes          | Like and Unlike Observations - As a user I can like / unlike observations and comments so that I can highlight my interest in the content. | Create Likes Serializer                 |
| Likes          | View liked observations - As a user I can easily locate observations I have liked so that I can stay up to date with comments / updates.   | Create LikeList View                    |
| Likes          | View liked observations - As a user I can easily locate observations I have liked so that I can stay up to date with comments / updates.   | Create LikeDetail View                  |

## Models and CRUD breakdown
![model-crud](/docs/screenshots/model-crud.png)

## Entity Relationship Diagram
![relationship-diagram](/docs/screenshots/relationship-diagram.png)

## Testing
### Validator
All errors in GitHub Problems resolved excluding the below exceptions.

#### *settings.py AUTH_PASSWORD_VALIDATORS*<br>
![settings-problems](/docs/screenshots/settings-problems.png)

#### *env.py DATABASE_URL*<br>
![env-problems](/docs/screenshots/env-problems.png)

### Automated
-   [Observations](/observations/tests.py)
    -   test_can_list_observations
    -   test_logged_in_user_can_create_observation
    -   test_user_not_logged_in_cant_create_observation
    -   test_can_retrieve_observation_using_valid_id
    -   test_cant_retrieve_observation_using_invalid_id
    -   test_user_can_update_own_observation
    -   test_user_cant_update_another_users_observation
-   [Comments](/comments/tests.py)
    -   tba
-   [Likes](/likes/tests.py)
    -   tba
-   [Profiles](/profiles/tests.py)
    -   tba

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
