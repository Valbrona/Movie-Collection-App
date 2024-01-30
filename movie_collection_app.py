menu_prompt = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = []

def add_movie():
    title = input("Enter a movie title: ")
    director = input("Enter the director of the movie: ")
    release_year = input("Enter the release year of the movie: ")

    movies.append(
        {
            "title": title,
            "director": director,
            "release_year": release_year
         }
    )


def list_movie():
    print("*" *10, "Your movie collection:" , "*" *10)
    for movie in movies:
        print(movie["title"])


def search_movie():
    found_movie = False
    find_movie = input("Please type in the movie: ")
    for movie in movies:
        if find_movie in movie["title"]:
            found_movie = True
            print(f" The movie {movie["title"]} is on your list.")
    if found_movie == False:
        print("Sorry, this movie does not exist on your list.")


def user_menu():
    selection = input(menu_prompt)
    while selection != "q":
        if selection == "a":
            add_movie()
        elif selection == "l":
            list_movie()
        elif selection == "f":
            search_movie()
        else:
            print("Unknown command. Please try again.")
        selection = input(menu_prompt)

user_menu()