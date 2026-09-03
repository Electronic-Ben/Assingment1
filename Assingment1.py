import os

def clear():
    os.system("cls")

class Problem:
    name = "Problem"

    def callback():
        print("UNASSIGNED")


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

class TrendingTracker(Problem):
    name = "Trendy"

    def callback(self):
        views = self.enter_views()
        time = self.get_time()

        print("You averaged about " + str(round(views/time, 3)) + " views per second")

    def enter_views():
        user_in = int(input("How many total views? "))
        return user_in
    
    def get_time():
        ans = input("Enter time (00h 00m 00s): ")

        segs = ans.split(' ')
        h = int(segs[0][:-1])
        m = int(segs[1][:-1])
        s = int(segs[2][:-1])

        return (h * 60 * 60) + (m * 60) + s
    

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
            print("Invalid input.")
            
            return self.get_function(self)
        
    def get_temp(self, func):
        ans = float(input("Enter temp to convert: "))
        return func(ans)

class TipCalculator(Problem):
    name = "Tip Calculator"

    def callback(self):
        bill = self.get_bill()
        percent = self.get_percent()
        split_tip = self.get_split(bill * percent / 100)

        print("Each person should tip $" + str(round(split_tip), 2))

    def get_bill():
        return float(input("What was you bill? (Enter: 000.00) "))
    
    def get_percent():
        return float(input("What percentage do you want to tip? "))
    
    def get_split(tip):
        return tip / int(input("How many poeple are splitting the tip? "))

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