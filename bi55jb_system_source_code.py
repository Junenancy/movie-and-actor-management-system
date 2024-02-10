
import random

class Movies:
    def __init__(self, title, year, genre, release_date):
        self.movie_id = random.randint(1000,9999)
        self.title = title
        self.year = year
        self.genre = genre
        self.release_date = release_date
    
    def set_title(self, title):
        """
        Method to set the title of the movie.
        
        Args: 
        - title: The title of the movie
        """
        if title and isinstance(title, str):
            self.title = title
        else:
            print("Error: Invalid title")
        
    def set_year(self, year):
        """
        Method to set the year of the movie.
        
        Args:
        - year: The year of the movie.
        """
        if year and isinstance(year, int) and 1900 <= year <= 2100:
            self.year = year
        else: print("Error: Invalid year")
        
    def set_genre(self, genre):
        """
        Method to set the genre of the movie.
        
        Args:
        - genre: The genre of the movie
        """
        if genre and isinstance(genre, str):
            self.genre = genre
        else: 
            print("Error: Invalid genre")
            
    def set_release_date(self, release_date):
        """
        Method to set the release date of the movie.
        
        Args:
        - release_date: The release date of the movie.
        """
        if release_date and isinstance(release_date, str): 
            self.release_date = release_date
        else: 
            print('Error: Invalid release date')
        
    def get_title(self):
        """
        Method to retrieve the title of the movie.
        
        Returns:
        The title of the movie.
        """
        return self.title
        
    def get_year(self):
        """
        Method to retrieve the year of the movie.
        
        Returns: 
        The year of the  movie.
        """
        return self.year
        
    def get_genre(self):
        """
        Method to retrieve the genre of the movie
        
        Returns:
        The genre of the movie.
        """
        return self.genre
        
    def get_release_date(self):
        """
        method to retrieve the release date of the movie.
        
        Returns:
        The release date of the movie.
        """
        return self.release_date
        
class MovieList:
    def __init__(self):
        self.movie_collection = {}
        
    def add_movie(self, movie: Movies):
        """
        Method to store a collection of movie objects in the movieList.
        
        Args:
        - movie: Movie object to be added to the collection.
        """
        if isinstance(movie, Movies):   
            self.movie_collection[movie.movie_id] = movie
        else:
            print("Error: Invalid movie object")
            
    def search_movies(self, attribute, value):
        """
        Method to search for movies in the collection based on the specifified attribute and value
        
        Args:
        - attribute: Attribute to search for (e.g., 'title', 'genre', release_date',).
        - value: VAlue to match for the specified attribute.
        
        Returns:
        A list of matching movies.
        """
        matching_movies = []
        for movie in self.movie_collection.values():
            if attribute == "title" and movie.title == value:
                matching_movies.append(movie)
            elif attribute == "year" and movie.year == value:
                matching_movies.append(movie)
            elif attribute == "genre" and movie.genre == value:
                matching_movies.append(movie)
            elif attribute == "release_date" and movie.release_date == value:
                matching_movies.append(movie)
        return matching_movies
                   
    def remove_movie(self, title):
        """
        Method to remove a movie from the collection based on the title.
        
        Args: 
        - title: Title of the movie to be removed.
        """
        for movie_id, movie in list(self.movie_collection.items()):
            if movie.title == title:
                del self.movie_collection[movie_id]
        
    def get_total_movies(self):
        """
        Method to calculate and return the total number of movies stored in the collection.
        
        Returns:
        Total number of movies
        """
        return len(self.movie_collection)
        
class Actors:
    def __init__(self, firstname, surname, gender, date_of_birth):
        self.firstname = firstname
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth
        
    def set_firstname(self, firstname):
        """
        Method to set the first name of the actor.
        
        Argss:
        - firstname: The firstname of the actor
        """
        if firstname and isinstance(firstname, str):
            self.firstname = firstname
        else:
            print("Error: Invalid first name")
            
    def set_surname(self, surname):
        """
        Method to set the surname of the actor
        
        Args:
        - surname: The surname of the actor.
        """
        if surname and isinstance(surname, str):
            self.surname = surname 
        else:
            print("Error: Invalid surname")
            
    def set_gender(self, gender):
        """
        Method to set the gender of the actor.
        
        Args: 
        - gender: The gender of the actor.
        """
        if gender and isinstance(gender, str):
            self.gender = gender
        else:
            print("Error: Invalid gender")
            
    def set_date_of_birth(self, date_of_birth):
        """
        Method to set the date of birth of the actor
        
        Args:
        - date_of_birth: The date of birth of the actor.
        """
        if date_of_birth and isinstance(date_of_birth, str):
            self.date_of_birth = date_of_birth
        else:
            print("Error: Invalid date of birth")
    def get_firstname(self):
        """
        Method to retrieve the first name of the actor.
        
        Returns: 
        The first name of the actor.
        """
        return self.firstname
        
    def get_surname(self):
        """
        Method to retrieve the surname of the actor.
        
        Returns:
        The surname of the actor
        """
        return self.surname
        
    def get_gender(self):
        """
        Method to retrieve the gender of the actor.
        
        Returns:
        The gender of the actor.
        """
        return self.gender
        
    def get_date_of_birth(self):
        """
        Method to retrieve the date of birth of the actor
        
        Returns:
        The date of birth of the actor.
        """
        return self.date_of_birth
        
class ActorList:
    def __init__ (self):
        self.actor_collection = []
        
    def add_actor(self, actor: Actors):
        """
        Method to add and store a collection of actor objects.
        
        Args:
        - actors: A list of Actors objects to be stored in the collection.
        """
        if isinstance(actor, Actors):
            self.actor_collection.append(actor)
        else:
            print("Error: Invalid actor object")
            
    def remove_actor(self, firstname):
        """
        Method to remove an actor from the collection by providing the actor's firstname.
        This operation informs the user if there are two or more actors with the same first name
        
        Args:
        - firstname: The first name of the actor to be removed.
        """
        matching_actors = [actor for actor in self.actor_collection if actor.firstname.lower() == firstname.lower()]
        
        if not matching_actors:
            print(f"Error: Actor with the first name '{firstname}' not found.")
            return
        
        if len(matching_actors) == 1:
            actor = matching_actors[0]
            self.actor_collection.remove(actor)
            print(f"Actor '{actor.firstname}' removed successfully")
        else:
            print(f"Multiple actors found with the first name '{firstname}'.")
            print("Please provide additonal information to identify the actor\n:")
            
            additional_info = input("Enter additional information (e.g., date of birth, gender, surname)\n:")
            
            matching_actors = [actor for actor in matching_actors 
                               if actor.surname.lower() == additional_info.lower() 
                               or actor.date_of_birth.lower() == additional_info.lower() 
                                or actor.gender.lower() == additional_info.lower()]
            
            if not matching_actors:
                print("Error: Actor with the first name '{firstname}' not found based on provided information.")
            elif len(matching_actors) == 1:
                actor = matching_actors[0]
                self.actor_collection.remove(actor)
                print(f"Actor '{actor.firstname}' removed successfully") 
            else:
                print("Error: Unable to uniquely identify the actor based on the provided information.")
                       
    def get_total_actors(self):
        """
        Method to get total  number of actors in the system
        
        returns:
        - The total number of actors in the collection
        """
        return len(self.actor_collection)
        
    def get_actor_details(self, firstname):
        """
        Method to iterate through all the objects stored in the collection
        and return the details of an actor based on the first name of the actor
        
        Args: 
        - firstname: The first name of the actor.
        
        Returns
        - A dictionary containing the details of the actor if found, otherwise None
        """
        matching_actors = [actor for actor in self.actor_collection if actor.firstname == firstname]
        
        if matching_actors:
            return matching_actors[0].__dict__
        else:
            return None
    
# Testing the system
def test_system():
        
# Creating movie Object
    movie_007 = Movies("007: Casino Royale", 2007, "action", "21st Jan 2007")
      
# Creating actor Object 
    james_bond = Actors("James", "Bond", "Male", "24th May 1964")
      
# Creating movie list object 'actions'
    actions = MovieList()
    actions.add_movie(movie_007)
      
# Creating actor list object 'all_actors'
    all_actors = ActorList()
    all_actors.add_actor(james_bond)
      
# Testing statements

# Get all details of movie '007'
    print("The details of movie '007':\n", actions.search_movies("title","007: Casino Royale")[0].__dict__)
    [print(f"{key}:{values}") for details in actions.search_movies("title","007: Casino Royale")[0].__dict__ for keys, value in details.items()] or None
# Get the number of actors in the system
    print("Number of actors in the system:\n", all_actors.get_total_actors())
    
    # Get details of actor 'James Bond'
    actor_details = all_actors.get_actor_details("James")
    
    if actor_details:
        print("Details of actor 'James Bond:", actor_details)
        
    else:
        print(f"Error: Actor 'James Bond' not found.")
        
    # Remove actor 'James Bond' not found.
    all_actors.remove_actor("James")
        
# Get the number of actors in the system after removal
    print("Number of actors in the system after removal:", all_actors.get_total_actors())
     
test_system()
    
        
         
         
    
    
        
    
