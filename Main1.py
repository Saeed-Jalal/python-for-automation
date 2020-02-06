
bill = 47.28
tip = bill * 15 / 100
total = bill + tip
share = total / 2
print("Each person needs to pay: " + str(share))
# Useage of function
def greetings(name, department):
    print("Good Day! " + name)
    print("You are part of " + department)
greetings("Muhammad Saeed ", " AI")

def welcoming(name, compnay):
    print("We would like to offically welcome you, " + name)
    print("To the Worlds best compny " + compnay)
welcoming("Saeed", "Google")
welcoming("Jenifor", "TechSofter")
welcoming("Samantha", "TechSofter")

def welcome_greetings(name, department):
    print("We Welcome you, " + name +"." + "You are the part of TechSofter " + department +".")

welcome_greetings("Saeed", "Exective Team")
welcome_greetings("Jason", "Marketing Team")
welcome_greetings("Emily", "Business Team")
welcome_greetings("Shoaib", "Software Development") 

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

def lucky_number(name):
    number = len(name)  * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Saeed")
lucky_number("Shoiab")


def print_seconds(hours, minutes, seconds):
    print(hours * 3600 + minutes * 60 + seconds * 1)

print_seconds(1, 2, 3)

# Principles of Code Reuse  example
june_hours = 243
june_cost = june_hours * 0.65
print("In June we spent: " + str(june_cost))

july_hours = 325
july_cost = july_hours * 0.65
print("In July we spent: " + str(july_cost))

august_hours = 298
august_cost = august_hours * 0.65
print("In August we spent: " + str(august_cost))

# The above example by reusing code

def print_monthly_expense(month, hours):
    cost = hours * 0.65
    print("The expense for the " + month + " are: " + str(cost))


print_monthly_expense("June", 243)
print_monthly_expense("July", 325)
print_monthly_expense("August", 298)



