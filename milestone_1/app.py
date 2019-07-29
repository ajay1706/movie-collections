# Enter 'a' to add movie, '1' to see your movies , 'f' to find a movie , and 'q' to quir

# Add movies
#see movies
# find movies
#stop running the program

#Tasks:
""""
[x]: Decide where to store movies
[]: What is the format of the movie.
[x]:Show the user the main interface and get their input.
[]: Allow users to add movies.
[]: Show all their movies
[]: Find a movie
[x]: Stop running the program when they type 'q'
"""

movies = []
"""
movies = {
'name': ... {str},
'director':...{str}
'year' : {int}


"""




def menu():
    user_input = input("Enter 'a' to add movie, '1' to see your movies , 'f' to find a movie , and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movies()
        elif user_input == 'q':
            print("Stopping program....")

        else:
            print("Unknown command ")


        user_input = input("Enter 'a' to add movie, '1' to see your movies , 'f' to find a movie , and 'q' to quit")


def add_movie():
    name = input("Enter a movie name : ")
    director = input("Enter a director name: ")
    year = int(input("Enter a movie year: "))

    movies.append({
        'name' : name,
        'director': director,
        'year': year
    })




menu()
print(movies)

