# def greet(name):
#     print("Hello", name)


# greet("Dalton")
# greet("Steam")
# greet("League")


def favorite_game(game):
    print("My favorite game is", game)

favorite_game("Deadlock")
    
def add(a, b):
    print("answer = ", a+b)

add(7,2)

def age_check(age):
    if age >= 18:
        print("Access Granted")
    else:
        print("Access Denied")

age_check(age = 12)
age_check(age= 18)
age_check(age= 100)
age_check(age= 99999999)

def clicked(item):
    if item == "League of Legends":
        print (item)
    elif item == "Deadlock" :
        print("Opening", item)
    else:
        print ("page not found")

clicked(item = "League of Legends")
clicked(item = "Deadlock")
clicked(item = "XXX")

def game_status(game):
    if game == "League of Legends":
        return "Installed"
    else:
        return "Not Installed"
    
print(game_status("League of Legends"))
print(game_status("Minecraft"))

def open_page(page):
    if page == "League Rank":
        return "Opening League Rank page..."
    elif page == "Current Balance":
        return "Opening Current Balance page..."
    else:
        return "Page", page, " does not exist."
    
print(open_page("League Rank"))
print(open_page("XXX"))

page = "League Rank"

message = "Opening " + page + " page..."

print(message)