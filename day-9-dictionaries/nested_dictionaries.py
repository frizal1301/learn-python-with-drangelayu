# Nesting dictionaries in dictionaries
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 20},
    "Germany" : {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12}
}

# Nesting dictionaries in list
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 20,
    },
    {
        "country": "Germany",  
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 12
    }
]
# 2 Ways to append a dictionaries to a list
travel_log.append({
        "country": "Inoonesia",  
        "cities_visited": ["Jakarta", "Bali", "Makassar"], 
        "total_visits": 1
})

new_country = {}
new_country["country"] = "Malaysia"
new_country["cities_visited"] = ["Kuala Lumpur", "Sabah", "Selangor"]
new_country["total_visits"] = 3

travel_log.append(new_country)
print(travel_log)

family = {
    "father": "Mahasiswa",
    "mother": "Cahaya Bulan",
    "child1": "Fahru Rizal",
    "child2": "Nurul Fajril Ilmah"
}
print(family["father"])