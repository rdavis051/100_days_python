# Dictionary
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
    "USA" : "Washington DC",
}
#print(capitals)
# Nesting Dictionary in a Dictionary

travel_log_old = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#print(travel_log_old)
# Nesting Dictionary in a List

travel_log = [
    {
        "country" : "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country" : "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 5
    },
]
#print(travel_log)

# function that adds to the travel_log
def add_new_country(country, visits, list_of_cities):
    tmp_dict = {
        "country" : country,
        "cities_visited" : list_of_cities,
        "total_visits" : visits,
    }
    travel_log.append(tmp_dict)

# User Entry
new_country = input("Please enter country: \n")
visited = int(input("Please enter times visited: \n"))
cities_list = []
more_cities = True
while more_cities == True:
    city = input("Please Enter the city: \n").lower()
    cities_list.append(city)
    add_city = input("Do you have another city to enter (Y/y): \n").lower()
    if add_city == 'y':
        more_cities = True
    else:
        more_cities = False

add_new_country(new_country, visited, cities_list)

print(travel_log)
print()
print("====================================")
print()
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['total_visits']} times.")
print(f"My favorite city was {travel_log[2]['cities_visited'][0]}.")
