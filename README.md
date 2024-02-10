Programming Tasks
Design and implement a software system for a fictitious movie management system. Your system should follow object oriented 
programming approach. It should contain the following components each represented in a Python class:
• Movies: Define a Python class with methods to do the following: 
1. Define a constructor to create new move records with the following details:
a. Randomly generated ID, title, year, genre and release date. 
2. Define different methods for setting the following details. You should have one method for each detail:
a. title, year, genre and release date.
3. Define different methods to retrieve the following detail. You should have one method for each detail: 
a. title, year, genre and release date 
4. You should include appropriate error checking and detailed comments in our code.
• MovieList: Define a Python class with methods to do the following: 
1. Define a constructor to create an object of the MovieList class.
2. A method to store a collection of movie objects that are created using the Movie class above. You should use a dictionary 
for to store the items with appropriate keys and values.
3. A method to search through the collection and find a movie by one or more of the following movie attributes: title, genre 
or release date.
4. A method to remove a movie from the collection based on the title of the movie.
5. A method to calculate and return the total number of movies stored in the collection. 
6. You should include appropriate error checking and detailed comments in our code.
• Actors: Define a Python class with functions to do the following: 
1. Define a constructor to create new actor records with the following details:
o First name, surname, gender and date of birth.
2. Define different methods for setting the following details. You should have one method for each detail: actor’s first
name, surname, gender and date of birth. 
3. Define different methods for retrieving the following details. You should have one method for each detail: actor’s first
name, surname, gender and date of birth.
4. You should include appropriate error checking and detailed comments in our code.
• ActorsList: Define a Python class with functions to do the following:
1. Define a constructor to create an object of the ActorsList class.
2. A method to store a collection (e.g., dictionary, lists, tuple etc.) of actors objects that are created with the class Actors. 
3. A method to remove an actor (object) from the collection by giving the actor’s first name. This operation must inform 
program users if there are two or more actors with same first name. 
4. A method to count the number of actors in the system.
5. A method to iterate through all the objects stored in the collection and return the details of an actor based on the first
name of the actor.
6. You should include appropriate error checking and detailed comments in our code.
• System testing: Write a python module to include appropriate code to automatically create the following objects:
1. A movie object named ‘007’ with all the details required for a movie. 
2. A movie list object named ‘actions’ that contains ‘007’ object in the object’s collection. 
3. An actor object named ‘JamesBond’ with all the details required for an actor in the class. 
4. An actor list object named ‘all_actors’ that contains ‘JamesBond’ object in the object’s collection.
5. A statement to call the movie object method to get all the detail of the movie object “007”. 
6. A statement to call the actor list object method to get the number of objects in its collection. 
7. A statement to call the actor list object method to get the details of the actor James Bond
8. A statement to call the actor list object method to remove the details of the actor James Bond from the collection
