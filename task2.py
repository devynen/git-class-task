"""
Task 2: Film Night Prep
You're helping your community plan a Friday Film Night for kids. The initial list of movie genres to be shown includes:
genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]

1. Add the genre "Drama" at the end of the list because parents requested it.
2. Someone mistakenly added "Fantasy" twice. Make sure there's only one "Fantasy" in the list.
3. The organizer wants to know how many genres are now planned to be shown.
4. Display the second and second-to-last genres to verify diversity.

→ Modify the list and display the required results.
"""



genres = ["adventure", "comedy", "animation", "fantasy", "sci-Fi", "documentary", "fantasy"]

#to add drama to the end of list
genres.append("drama") 
print(genres)

#to  delete one "fantasy" 
del genres[-2:-1]
print(genres)

#to show how many genres will be shown
total_genres = len(genres)
print(f"total genres to be shown",total_genres)


#to display second genre
second_genre = genres[1]
print(f"second genre is",second_genre)

#to display second to the last genre 
second_to_the_last = genres[-2]
print(f"second to the last genre is",second_to_the_last)  



