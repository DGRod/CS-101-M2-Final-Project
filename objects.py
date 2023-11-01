import csv

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value
    
    def set_next_node(self, new_node):
        self.next_node = new_node
    
    def get_next_node(self):
        return self.next_node
    
    


class LinkedList:
    def __init__(self, name, head_node=None):
        self.name = name
        self.head_node = head_node
    
    def __repr__(self):
        return self.name

    def add_head(self, new_head_value):
        new_head_node = Node(new_head_value)
        new_head_node.set_next_node(self.head_node)
        self.head_node = new_head_node

    def traverse(self):
        string = ""
        current_node = self.head_node
        while current_node:
            string += (str(current_node.get_value()) + "\n")
            current_node = current_node.get_next_node()
        print(string)




class Country:
    def __init__(self, name, population, region, area, gdp):
        self.name = name
        self.population = population
        self.region = region
        self.area = area
        self.gdp = gdp

    def __repr__(self):
        return self.name


north_america = LinkedList("North America")
south_america = LinkedList("South America")
carribean = LinkedList("Carribean")
europe = LinkedList("Europe")
middle_east = LinkedList("Middle East")
north_africa = LinkedList("North Africa")
sub_saharan_africa = LinkedList("Sub-Saharan Africa")
central_asia = LinkedList("Central Asia")
south_asia = LinkedList("South Asia")
east_asia = LinkedList("East Asia")
oceania = LinkedList("Oceania")

regions = ["North America", "South America", "Carribean", "Europe", "Middle East", "North Africa", "Sub-Saharan Africa", "Central Asia", "South Asia", "East Asia", "Oceania"]
linked_lists = [north_america, south_america, carribean, europe, middle_east, north_africa, sub_saharan_africa, central_asia, south_asia, east_asia, oceania]

region_dict = dict(zip(regions, linked_lists))



with open("country_pop_chart.csv", "r") as csv_file:
    data_dict = csv.DictReader(csv_file)
    
    for row in data_dict:
        for key, value in region_dict.items():
            if row['Region'] == key:
                value.add_head(Country(row['Name'], row['Population'], row['Region'], row['Area'], row['GDP']))


regional_list = LinkedList("Regional List")

for list in linked_lists:
    regional_list.add_head(list)

#middle_east.traverse()