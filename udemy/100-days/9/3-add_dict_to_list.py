travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, times, cities):
    new_country = {
        "country": country,
        "visits": times,
        "cities": cities
    }
    travel_log.append(new_country)
    
    print(f"I've been to {country} {times} times.")
    print(f"My favourite city was {cities[0]}.")



add_new_country("India", 3, ["Kochi", "Hyderabad", "Bangalore"])

# we want to add a dict to a list
# we created the dic, then we appended it to the list

