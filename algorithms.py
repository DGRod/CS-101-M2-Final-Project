from objects import regional_list, north_africa, LinkedList


def search_list(linked_list, target):
    current_node = linked_list.head_node

    while current_node:
        if str(current_node.value) == target:
            return current_node.value
        current_node = current_node.get_next_node()

    return None

def dfs(double_linked_list, target):
    current_sublist = double_linked_list.head_node

    while current_sublist:
        target_present = search_list(current_sublist.value, target)
        if target_present:
            return target_present
        else:
            current_sublist = current_sublist.get_next_node()

    print("\nCountry not found")
    return None


def find_data(double_linked_list, target, data):
    country = dfs(double_linked_list, target)
    processed_data = (data.strip()).title()
    initials = {"P":country.population, "R":country.region, "A":country.area, "G":country.gdp}

    if processed_data[0] in initials:
        result = initials[processed_data[0]]
        return result, processed_data[0]
   
    return "Available information for " + target + ":\nPopulation\nRegion\nArea\nGDP\nPlease select one of these options."
    

def printer(country, result, data_initial):
    if data_initial == "P":
        print("The population of " + country + " is: " + result)
    if data_initial == "R":
        print(country + " is located in the " + result + " region.")
    if data_initial == "A":
        print(country + " has an area of " + result + " km^2")
    if data_initial == "G":
        print(country + " has a GDP of " + result)



#search_list(regional_list, "North Africa").traverse()

#print(dfs(regional_list, "Kosovo"))

welcome = "Welcome to the Python Country Database!"
print(welcome)

country = input("What country would you like to search for?\n").title()
country_exists = dfs(regional_list, country)

while country_exists == None:
    country = input("Please enter the name of a recognized country:\n").title()
    country_exists = dfs(regional_list, country)
    if country_exists != None:
        break
    continue


initials = ["P", "R", "A", "G"]
data = input("\nWhat information about " + country.title() + " would you like?\nYou can find the Population, Region, Area, or GDP\n")
data_exists = data.title()[0] in initials

while data_exists == False:
    data = input("\nAvailable information for " + country + ":\nPopulation\nRegion\nArea\nGDP\n\nPlease select one of these options:\n")
    data_exists = data.title()[0] in initials
    if data_exists == True:
        break
    continue


rd = find_data(regional_list, country, data)

printer(country, rd[0], rd[1])


