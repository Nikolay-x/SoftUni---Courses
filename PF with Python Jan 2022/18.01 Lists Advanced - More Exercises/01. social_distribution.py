# 1.Social Distribution
# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what, and that is exactly what you are called to do for this problem.
# On the first line, you will be given the population (numbers separated by comma and space ", "). On the second line, you will be given the minimum wealth. You should distribute the wealth so that no part of the population has less than the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population.
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible".
#
# Input
# 2, 3, 5, 15, 75
# 5
#
# Output
# [5, 5, 5, 15, 70]

population_wealth = list(map(int, input().split(", ")))
minimum_wealth = int(input())

is_possible = True

for pop in population_wealth:

    max_pop = max(population_wealth)
    max_pop_index = population_wealth.index(max_pop)
    pop_index = population_wealth.index(pop)

    if pop < minimum_wealth:
        population_wealth[max_pop_index] -= minimum_wealth - pop
        population_wealth[pop_index] = minimum_wealth
        if population_wealth[max_pop_index] < minimum_wealth:
            is_possible = False

if is_possible:
    print(population_wealth)
else:
    print("No equal distribution possible")
