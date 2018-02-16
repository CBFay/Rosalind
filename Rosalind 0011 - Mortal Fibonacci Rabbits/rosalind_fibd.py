file = open("rosalind_fibd.txt")
N, M = map(int, file.read().split(" "))
file.close()

class rabbit_pair:
    def __init__(self, ID):
        self.age = 0
        self.ID = ID


def rabbit_population(n, m):
    """
    n : Months passed
    m : Life Expectancy
    """
    
    iden = 2
    population = [rabbit_pair(1)]
    for months in range(n):
        next_gen = []
        print('MONTH', months)
        print('POPULATION', len(population))
        for rabbits in population:
            print('\trabbit:', rabbits.ID, 'age:', rabbits.age)
            if rabbits.age > 0 and rabbits.age < m:
                next_gen.append(rabbit_pair(iden))
                iden += 1
                print('\tbirth')
            rabbits.age += 1
            print()
        for baby in next_gen:
            baby.age += 1
        population.extend(next_gen)
    return len([r for r in population if r.age < m])

print(rabbit_population(N, M))
