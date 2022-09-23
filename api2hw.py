from colorama import Fore, Style, init
import requests,json
init()

#url = f"http://www.boredapi.com/api/activity?minprice=:{minprice}&maxprice=:{maxprice}-"

#def func(a,b):
    #a = int(input("Enter the lowest amount you're willing to spend. "))
    #b = int(input("Enter the highest amount you're willing to spend. "))

class Retrieve_acts():
    def __init__(self):
        self.activity = ""
        self.type = ""
        self.participants = None
        self.price = None

    def search_Act(self):
        minprice = input("Enter the lowest amount you are willing to spend, between 0 and 1: ")
        maxprice = input("Enter the highest amount you are willing to spend, between 0 and 1: ")
        url= f"http://www.boredapi.com/api/activity?minprice={minprice}&maxprice={maxprice}"
        response = requests.get(url)
        data = response.json()
        if not response.ok:
            return False
        else:
            self.activity = data["activity"]
            self.type = data["type"]
            self.participants = data["participants"]
            self.price = data["price"]
        return True


    def print_off(self):
        print(Fore.BLUE ,end="")
        print(self.activity ,end=" ")
        print(Fore.RED ,end="")
        print(self.type ,end=" ")
        print(Fore.YELLOW ,end="")
        print(self.participants ,end=" ")
        print(Fore.GREEN ,end="")
        print(self.price ,end=" ")
        print(Style.RESET_ALL)
    
    def final_prompt(self):
        prompt = Retrieve_acts()
        while True:
            print(prompt.search_Act())
            prompt.print_off()
            option = input("If you would like to continue searching for activities press ENTER. If not, type quitT? ")
            if option == "quit":
                print("Thank you for using our services!")
                break

prompt = Retrieve_acts()
prompt.final_prompt()