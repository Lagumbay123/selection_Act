def chinese_zodiac(year):
    animals = ['monkey', 'rooster', 'dog', 'pig', 'rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep']
    return animals[year % 12]

year = int(input("Enter a year: "))
print("The Chinese Zodiac sign for the year", year, "is", chinese_zodiac(year))
