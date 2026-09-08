import os
import math

def clear():
    os.system("cls")

def get_float(message):
    try:
        ans = float(input(message))
    except Exception as e:
        print("Invalid.")
        return get_float(message)
    return ans

def get_int(message):
    try:
        ans = int(input(message))
    except Exception as e:
        print("Invalid.")
        return get_int(message)
    return ans

class Problem:
    name = "Problem"

    def callback():
        print("UNASSIGNED")

'''
Using print() statements and your imagination, write a function called display_logo() that shows a
unique logo you can add to your programs. The logo should be at least 5 lines tall and use at least 3
different characters.
Demonstrate your function works by calling it from the main part of your program.
'''

class Logo(Problem):
    name = "Logo"

    def callback(self):
        self.display_logo(self)

    def display_logo(self):
        print(
            "  0 0  \n"
            ".  )  . \n"
            " \\===/ "
        )

'''
In preparation for your future career providing live streaming coverage, you're going to make a
program to help measure the popularity of a stream.
The user should enter the total number of views and the hours, minutes, and seconds that have
passed since the start of the stream. The output should be the ratio of viewers per second.
Create a function that converts hours/minutes/seconds into total seconds, and another function that
calculates and returns the viewers-per-second ratio.
'''

class TrendingTracker(Problem):
    name = "Trendy"

    def callback(self):
        views = self.enter_views()
        time = self.get_time()

        print("You averaged about " + str(round(views/time, 3)) + " views per second")

    def enter_views():
        user_in = get_int("How many total views? ")
        return user_in
    
    def get_time():
        
        h = get_int("Enter hours streamed: ")
        m = get_int("Enter minutes streamed: ")
        s = get_int("Enter seconds streamed: ")

        return (h * 60 * 60) + (m * 60) + s
    
'''
Write a program with two functions: one that converts Fahrenheit to Celsius, and one that converts
Celsius to Fahrenheit.
The program should let the user choose which conversion they need, enter a value, and get the result
formatted to two decimal places.
'''

class TempConverter(Problem):
    name = "Temperature Converter"

    def callback(self):
        func, symbol = self.get_function(self)
        temp = self.get_temp(self, func)
        
        print("That's about " + str(round(temp, 3)) + " degrees in " + symbol)

    def get_function(self):
        ans = input("Convert temp from F or C? (Enter F or C): ")
        if ans.lower() == 'f':
            return [lambda x: (x - 32) * 5.0 / 9.0, ans.upper()]
        elif ans.lower() == 'c':
            return [lambda x: (x * 9.0/5.0) + 32, ans.upper()]
        else:
            print("Invalid.")
            return self.get_function(self)
        
    def get_temp(self, func):
        ans = get_float("Enter temp to convert: ")
        return func(ans)

'''
Write a program that helps restaurant patrons calculate tips. Create functions that:
 - Calculate the tip amount given a bill and percentage
 - Calculate the total including tip
 - Calculate how to split the bill among a group
Let the user enter their bill amount, preferred tip percentage, and number of people splitting. Display
a nicely formatted summary.
'''

class TipCalculator(Problem):
    name = "Tip Calculator"

    def callback(self):
        bill = self.get_bill()
        percent = self.get_percent()
        split = self.get_split()
        tip = bill * percent / 100

        print("\nTotal Bill: $" + str(bill))
        print("Tip Percentage: " + str(percent))
        print("Number of people: " + str(split))
        print("\nEach person should tip $" + str(round(tip / split, 2)))

    def get_bill():
        return get_float("What was you bill? (Enter: 000.00) ")
    
    def get_percent():
        return get_float("What percentage do you want to tip? ")
    
    def get_split():
        return get_int("How many poeple are splitting the tip? ")

class Challenge(Problem):
    name = "Stage Light Calculator"

    def callback(self):
        [shutter_angle, dist] = self.calc_angle()
        brightness = self.calc_brightness(dist)

        if shutter_angle >= 90 or shutter_angle <= -90:
            print("Settings not possible. Try again.")
            clear()
            self.callback(self)
            return
        
        print("\nThe needed shutter angle is " + str(round(shutter_angle, 3)) + " degrees.")
        print("The stage will be lit with " + str(round(brightness, 3)) + " lumens per square meter.")

    def calc_angle():
        lense_dia = get_float("Diameter of lense: ")
        light_dia = get_float("Diameter of expected light circle: ")
        dist = get_float("Distance of light from stage: ")

        opp = (light_dia / 2) - (lense_dia / 2)
        
        return math.atan(opp / dist), dist

    def calc_brightness(dist):
        lumens = get_float("Brightness in lumens: ")

        return lumens / (dist * dist)




class Menu:
    problems = []
    selected = 0

    def display(self):
        clear()
        print("  Choose Problem to View")
        print("--------------------------")
        print("enter to change selection")
        print("'v' to view\n")
        
        for i in range(len(self.problems)):
            problem = self.problems[i]
            if i == self.selected:
                print(problem.name.upper())
            else:
                print(problem.name)

    def add_problem(self, problem):
        self.problems.append(problem)

    def  cycle_menu(self):
        self.selected = (self.selected + 1) % len(self.problems)

    def select_problem(self):
        clear()
        
        problem = self.problems[self.selected]
        
        print("Problem: " + problem.name + '\n')

        problem.callback(problem)

def init_menu(menu):
    menu.add_problem(Logo)
    menu.add_problem(TrendingTracker)
    menu.add_problem(TempConverter)
    menu.add_problem(TipCalculator)
    menu.add_problem(Challenge)
    
def main_loop():
    run = True
    menu = Menu()

    init_menu(menu)

    while run:
        
        menu.display()
        
        user_in = input()
        if user_in.lower() == 'v':
            menu.select_problem()
            input("\nEnter to return\n")
            menu.selected = 0
        else:
            menu.cycle_menu()

        

main_loop()