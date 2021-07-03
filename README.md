# TRACC

## Project Overview
- ### Elevator Pitch
	- **TRACC** is an acronym for "**t**racking **r**eal-time **a**ctivity of **c**limate **c**hange". It is a single-page web application that displays current weather data, but also past patterns and historical moments to showcase how climate change is affecting you and your surrounding area.

- ### Minimum Viable Product (MVP)

	- While the end goal is to do what I stated in the end goal, I will none the less, have not enough  time to do it. The minimum goal will be to save locations based on very basic user information. In addition, to just display current conditions at the given location.

 - ### Frameworks, Libraries, and APIs
	- I use **Free Weather API** ([Link](https://www.weatherapi.com/)) to access weather data, as it is freely offered from the government, and is often time, the main source of weather data for other APIs, so it is easiest just to stick to the source. This gives the added benefit of allowing me to access government-issued weather-related warnings (i.e. tornados, flooding, heatwaves, etc...)

	 - For CSS, I plan on using the **Bootstrap framework**, as I prefer it over Materialize and would like to get more comfortable with it. It goes without saying that I will also be using the **Django** and **VueJS** libraries, required via class curriculum.

 - ### Languages
	- I will be using **Python**, **JavaScript**, **CSS**, and **HTML** to develop the website.

- ### Source Control & Version Control
	- I will be using a **GitHub repository**, alongside **GitHub Desktop** to do source control. 
	
	- I will be using **Trello** for version control, to keep the project organized and flowing smoothly (even though there's just one develeoper!)

## Functionality

The user will be able to create an account with us, this data will be stored on a backend database. Once logged in, you will be able to save a location as a default or one of your favorites, in addition to adding new saved locations or removing old ones.

## Data Model

I will have a one-to-many data structure, wherein each user will have a: user-id-num, user-email, user-pass, and a list of saved locations. (If there is extra time, I will have an encryption system for all user data, or use google's system to store data safely. If there is not time to do that, then I will place a large warning over creating a new account, to ensure no one puts in data that they aren't worried about. And that this project is solely for educational and entertainment value)

## Schedule

As I learned from past development projects, "you should always budget 1.5x amount of time more than you think it will take you" (schedule 90min for a task you think will take 60min). Unfortunately I will be on vacation next week, and have a concurrent internship this week. So this does not leave me much time. Here is the planned schedule
| Day 1 (6/29) | Day 2 (6/30) |  Day 3 (7/01) |  Day 4 (7/02) |
|--|--|--| -- |
| Design & ideate. Create Github Repo and Trello Board; fill out trello board with tasks | Spend day working on creating a frontend skeleton and creating functionality | Spend day cleaning up frontend, and making an easy to use UI/UX. Implement user system and attach database | Catch up on any past missed issues or blockers |

If I have spare time during my vacation next week or over the weekend (Unfortunately I work on Saturdays) then I will spend it either improving the MVP if not yet completed. Or start a new sprint to work on adding additional features. 
