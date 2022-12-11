class Country:
    def __init__(self, country, capitol, population, square, continent):
        self.country = country
        self.capitol = capitol
        self.population = population
        self.square = square
        self.continent = continent

#  birth, deaths, immigration, emigration
#  + birth + immigration - deaths - emigration
    def population_growth_or_decline_per_year(self, birth, deaths, immigration, emigration):
        population_after_year = self.population + birth + immigration - deaths - emigration
        return population_after_year

    def __str__(self):
        return f'Continent {self.continent}, country {self.country}, capitol {self.capitol},' \
               f'population {self.population}'


poland = Country('Poland', 'Warsaw', 36_000_000, 40_000, 'Europe')
print(poland)
print(f'{poland.population_growth_or_decline_per_year(10_000, 20_000, 30_000, 50_000)}')
