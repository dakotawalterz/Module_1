import csv
with open("life-expectancy.csv", 'r') as system_file:
    csvreader = csv.reader(system_file, delimiter=',')
highest_expectancy = 0
highest_country = ""
highest_year = 0

lowest_expectancy = 999999
lowest_country = ""
lowest_year = 0
#the code above give us the base line for the high values and lowest values of our code!
print("\nWhat is the year and country that has the lowest life expectancy?")
print("What is the year and country that has the highest life expectancy?\n")

with open("life-expectancy.csv", 'r') as system_file:
    csvreader = csv.reader(system_file, delimiter=',')

    for line in system_file:
        clean_line = line.strip()    
        parts = clean_line.split(",")
        country = (parts[0])
        year = int(parts[2])
        expectancy = float(parts[3]) 
        
        if expectancy > highest_expectancy:
            highest_expectancy = expectancy
            highest_country = country
            highest_year = year
    
        if expectancy < lowest_expectancy:
            lowest_expectancy = expectancy
            lowest_country = country 
            lowest_year = year    
    
    print(f"The year and country with the lowest life expectancy is {lowest_country}, {lowest_year}.")
    print(f"The year and country with the highest life expectancy is {highest_country}, {highest_year}.\n")  

with open("life-expectancy.csv") as system_file: 
    highest_expectancy = 0
    highest_country = ""
    highest_year = 0

    lowest_expectancy = 999999
    lowest_country = ""
    lowest_year = 0   
    
    counter = 0
    sum_expectancy = 0
   
    given_year = int(input("Please enter a year between 1950 and 2019: "))
    
    for line in system_file:
        clean_line = line.strip()    
        parts = clean_line.split(",")
        country = parts[0]
        year = int(parts[2])
        expectancy = float(parts[3])  

        if year == given_year:
            sum_expectancy += expectancy
            counter += 1 
            
            if expectancy > highest_expectancy:
                highest_expectancy = expectancy
                highest_country = country
                highest_year = year

            if expectancy < lowest_expectancy:
                lowest_expectancy = expectancy
                lowest_country = country 
                lowest_year = year
    
    avg_expectancy = sum_expectancy/counter
    
    print(f"The average life expectancy for {given_year} was {round(avg_expectancy)} years.")
    print(f"The country with the lowest life expectancy for {given_year} was {lowest_country}.")
    print(f"The country with the highest life expectancy for {given_year} was {highest_country}.\n")
    
with open("life-expectancy.csv") as system_file:
    highest_expectancy = 0
    highest_country = ""
    highest_year = 0

    lowest_expectancy = 999999
    lowest_country = ""
    lowest_year = 0   
    
    counter = 0
    sum_expectancy = 0
    
    given_country = (input("Please enter a country:  "))
    
    for line in system_file:
        clean_line = line.strip()    
        parts = clean_line.split(",")
        country = parts[0]
        year = int(parts[2])
        expectancy = float(parts[3])  

        if country.lower() == given_country.lower():
            sum_expectancy += expectancy
            counter += 1 
            
            if expectancy > highest_expectancy:
                highest_expectancy = expectancy
                highest_country = country
                highest_year = year

            if expectancy < lowest_expectancy:
                lowest_expectancy = expectancy
                lowest_country = country 
                lowest_year = year
    
    avg_expectancy = sum_expectancy/counter
    
    print(f"The lowest and highest life expectancies for {given_country.capitalize()} were {round(lowest_expectancy)} and {round(highest_expectancy)}.")
    print(f"The average life expectancy for {given_country.capitalize()} is {round(avg_expectancy)} years.\n")
    