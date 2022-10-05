class Problem:
    def __init__(self, input):
        self.input = input
        self.numTasks = len(input)
    def cost(self, ans):
        totalTime = 0
        for task, agent in enumerate(ans):
            totalTime += self.input[task][agent]
        return totalTime


def Best_ans(population):

    min = solver.cost(population[0])
    index = 0
    for i in range(len(population)):
        cost = 0
        for task, agent in enumerate(population[i]):
            cost+=input[task][agent]
        if cost<min : 
            index = i
            min = cost
    return population[index]

import random
POP_size = 20
class GA:
    def __init__(self, solver):
        self.chromosomes = [[ j  for j in range(solver.numTasks)] for i in range(POP_size)]
        self.chromosomes_cost = [ 0 for i in range(POP_size)]
        self.chromosomes_fitness = [ 0 for i in range(POP_size)]
        self.chromosomes_p = [ 0 for i in range(POP_size)]
        self.parents = [ 0 for i in range(POP_size)]
        self.child = [ 0 for i in range(POP_size)]
        self.best = []

        while True :
            self.chromosomes_dup = [ 0 for i in range(POP_size)]
            for i in range(POP_size):
                random.shuffle(self.chromosomes[i])
                for j in range(solver.numTasks):
                    self.chromosomes_dup[i] += self.chromosomes[i][j]*pow(10, j)
            print('len : ', len(set(self.chromosomes_dup)))
            if len(set(self.chromosomes_dup)) == POP_size : break; 
            #檢查染色體有沒有重複 
        self.best = Best_ans(self.chromosomes)
        print('After shuffle : ', self.chromosomes)
        print('self.best: ', self.best)
        self.sol = solver

    def evaluate_fitness(self):
        for i in range(POP_size):
            self.chromosomes_cost[i] = self.sol.cost(self.chromosomes[i])
        cost_max = max(self.chromosomes_cost)
        cost_min = min(self.chromosomes_cost)
        for i in range(POP_size):
            self.chromosomes_fitness[i] = 1-(self.chromosomes_cost[i]-cost_min)/(cost_max-cost_min)

    def choise_parents(self):
        for i in range(POP_size):
            self.chromosomes_p[i] = round(self.chromosomes_fitness[i]/sum(self.chromosomes_fitness), 4)

        for i in range(POP_size):
            self.parents[i] = random.choices(self.chromosomes, self.chromosomes_p)[0]
            print(self.parents[i])
        print('parent = ', len(self.parents))
    
    def change(self, parent1, parent2):
        print('A : ', parent1)
        print('B : ', parent2)
        point = int(len(parent1)/2)
        print('point: ', point) #3
        cross_A = parent1[0:point]+parent2[point:]
        cross_B = parent2[0:point]+parent1[point:]
        print('cross A : ', cross_A)
        print('cross B : ', cross_B)
        print(parent1[point:])
        print(parent2[point:])
        cut_A=parent1[point:]
        cut_B=parent2[point:]
        C = [x for x in cut_A if x not in cut_B]
        D = [x for x in cut_B if x not in cut_A]
        print('C: ', C)
        print('D: ', D)
        for i in range(len(C)):
            index1 = cross_A.index(D[i], point, len(parent2))
            index2 = cross_B.index(C[i], point, len(parent1))
            print('index1 = ', index1)
            print('index2 = ', index2)
            cross_A[index1] = C[i]
            cross_B[index2] = D[i]
            print('cross A : ', cross_A)
            print('cross B : ', cross_B)
        return cross_A, cross_B

    def crossover(self):
        self.choise_parents()

        for i in range(0, POP_size, 2):
            self.child[i], self.child[i+1] = self.change(self.parents[i], self.parents[i+1])
        print('child : ', self.child)
    
    def mutate(self):
        

        


if __name__ == '__main__':
    input = [
    [10, 20, 23,  4],
    [15, 13,  6, 25],
    [ 2, 22, 35, 34],
    [12,  3, 14, 17]
    ]
    solver = Problem(input)
    ans=GA(solver)
    ans.evaluate_fitness()
    ans.crossover()


    #numAgents = len(input[0])
    #BFans = BF(numAgents)

    #yourAssignment = [3, 2, 0, 1] #⽤演算法得出的答案
    #solver = Problem(input)
    #print('Assignment:', BFans) # print 出分配結果
    #print('Cost:', solver.cost(BFans)) # print 出 cost 是多少