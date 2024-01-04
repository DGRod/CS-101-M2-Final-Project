# Python Country Database

## Background

## Python Code

### Modules
-This program imports the csv module

### Data Structures
- The Country class contains data on the population, region, area, and GDP of a given country.

- The LinkedList class describes a series of Node objects, each of which contains a single associated Country object. These nodes are organized into LinkedLists based on geographic region. A single 2-dimensional LinkedList is used to store each of these regional sublists into one masterlist containing all countries with available data.

### Country Data
- The data associated with each country is derived from Wikipedia and stored in a CSV file. This method of data storage was chosen so that any aspect of the country data could be updated easily without needing to make any manual changes within the program itself.

### Search Algorithms

- The search_list function is designed to traverse a LinkedList object in search of a certain target value

- The dfs function is designed to traverse a 2-dimensional LinkedList object in search of a certain target value

- The search_substring function is designed to traverse a 2-dimensional LinkedList object in search of any Country objects containing a name string whose initial characters match the input substring.

### User Interface

- The program begins with a welcome message and prompts the user to type in what country they would like to find information on.

- If the user's input is not a valid country name, the program will provide a list of autocomplete suggestions to their input and prompt the user to input a valid country name.

- Once the user has input a valid country name, the program will ask what type of data associated with that country they would like to see.

- After returning the appropriate data, the program will prompt the user to either continue searching or exit the database.

- All prompts for user input will return feedback if the player's input is unclear or a mistake. This prevents the program from breaking if the player makes a typo or other error and gives them another chance to input their choice.

## Further Improvements
- This program has many possibilities for future improvement. For example, it would be very straightforward to add more types of data associated with each country. It would also be possible to allow for a greater variety of queries and responses that can return a filtered list of countries or aggregate data from multiple countries.

## Conclusion
- Although simple, this program demonstrates how it is possible to import, organize, and retrieve real-world data in a Python program. And there are many directions in which this functionality could be expanded in the future.
