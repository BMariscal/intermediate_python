from matplotlib import pyplot

data = open("life_expectancies_usa.txt", "r").readlines()

year = []
life_men = []
life_women = []
for point in data:

    yearplot, life_men_plot, life_women_plot = (point.split(","))
    year.append(yearplot)
    life_men.append(life_men_plot)
    life_women.append(life_women_plot)



pyplot.plot(year,life_men, "bo-",label="Men")
pyplot.plot(year,life_women, "mo-",label="Women")
pyplot.legend(loc="upper left")
pyplot.ylabel("Average Life epectancy")
pyplot.xlabel("Year")
pyplot.title("Life expectancy for men and women")
pyplot.show()
