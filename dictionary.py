user = {}

user['name'] = input("enter your name: ")
user['age'] = int(input("enter your age: "))
user['fav_movies'] = input("enter your fav_movies seperated by comma ',': ").split(',')
user['fav_songs'] = input("enter your fav_songs seperated by comma ',': ").split(',')

for x,y in user.items():
    print(f"{x} : {y}")