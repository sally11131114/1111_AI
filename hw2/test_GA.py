class Problem:
    def __init__(self, input):
        self.input = input
        self.numTasks = len(input)
    def cost(self, ans):
        totalTime = 0
        for task, agent in enumerate(ans):
            totalTime += self.input[task][agent]
        return totalTime

import random
POP_size = 20
class GA:
    def __init__(self, solver):
        
        self.chromosomes = [[ j  for j in range(solver.numTasks)] for i in range(POP_size+20)]
        self.population = self.chromosomes[:10]+self.chromosomes[20:30]
        print('solver.numTasks', solver.numTasks)
        while True :
            self.chromosomes_dup = [ 0 for i in range(POP_size)]
            for i in range(POP_size):
                random.shuffle(self.population[i])
                for j in range(solver.numTasks):
                    self.chromosomes_dup[i] += self.population[i][j]*pow(10, j)
            
            print('len', len(set(self.chromosomes_dup)))
            if len(set(self.chromosomes_dup)) == POP_size : break 
            
            #檢查population size的染色體有沒有重複 
        print('After shuffle : ', self.population)
        self.sol=solver
        self.chromosomes_cost = [ 0 for i in range(POP_size)]
        self.chromosomes_fitness = [ 0 for i in range(POP_size)]

    def evaluate_fitness(self):
        for i in range(POP_size):
            self.chromosomes_cost[i] = self.sol.cost(self.population[i])
        print('cost : ', self.chromosomes_cost)
        cost_max = max(self.chromosomes_cost)
        cost_min = min(self.chromosomes_cost)
        print('max = ', cost_max, 'min = ', cost_min)
        for i in range(POP_size):
            self.chromosomes_fitness[i] = (self.chromosomes_cost[i]-cost_min)/(cost_max-cost_min)
        print('fitness : ', self.chromosomes_fitness)
        # temp = [i/sum(self.chromosomes_fitness[i]) for i in self.chromosomes_fitness]
        # print('fitness normed : ', temp)
        # test=[]
        # for i, x in enumerate(self.chromosomes_fitness):
        #     print('i=', i, 'x=', x)
        #     self.chromosomes_fitness[i] = (x-cost_min) / (cost_max-cost_min)
        # print('Normalized List:',self.chromosomes_fitness)

if __name__ == '__main__':
    input = [
    [10, 20, 23,  4],
    [15, 13,  6, 25],
    [ 2, 22, 35, 34],
    [12,  3, 14, 17]
    ]
    solver = Problem(input)
    Ans = GA(solver)
    Ans.evaluate_fitness()

    #numAgents = len(input[0])
    #BFans = BF(numAgents)

    #yourAssignment = [3, 2, 0, 1] #⽤演算法得出的答案
    #solver = Problem(input)
    #print('Assignment:', BFans) # print 出分配結果
    #print('Cost:', solver.cost(BFans)) # print 出 cost 是多少