import json
class Problem:
    def __init__(self, input):
        self.input = input
        self.numTasks = len(input)
    def cost(self, ans):
        totalTime = 0
        for task, agent in enumerate(ans):
            totalTime += self.input[task][agent]
        return totalTime


def Best_ans(solver, population):

    min = solver.cost(population[0])
    index = 0
    for i in range(len(population)):
        tmp_cost = solver.cost(population[i])
        if tmp_cost<min : 
            index = i
            min = tmp_cost
    return population[index]

def fact(num):
    if num == 0 : return 1
    if num >= 1 : return num*fact(num-1)

import random
class GA:
    def __init__(self, solver):
        self.POP_size = solver.numTasks*50#int(fact(solver.numTasks)/10)
        self.chromosomes = [[ j  for j in range(solver.numTasks)] for i in range(self.POP_size)]
        self.chromosomes_cost = [ 0 for i in range(self.POP_size)]
        self.chromosomes_fitness = [ 0 for i in range(self.POP_size)]
        self.chromosomes_p = [ 0 for i in range(self.POP_size)]
        self.parents = [ 0 for i in range(self.POP_size)]
        self.child = [ 0 for i in range(self.POP_size)]
        self.best = []
        self.sol = solver

        for i in range(self.POP_size):
            random.shuffle(self.chromosomes[i])
        #檢查染色體有沒有重複 

        self.best = Best_ans(self.sol, self.chromosomes)

    def evaluate_fitness(self):
        for i in range(self.POP_size):
            self.chromosomes_cost[i] = self.sol.cost(self.chromosomes[i])
        cost_max = max(self.chromosomes_cost)
        cost_min = min(self.chromosomes_cost)
        for i in range(self.POP_size):
            self.chromosomes_fitness[i] = 1-(self.chromosomes_cost[i]-cost_min)/(cost_max-cost_min)

    def choise_parents(self):
        for i in range(self.POP_size):
            self.chromosomes_p[i] = round(self.chromosomes_fitness[i]/sum(self.chromosomes_fitness), 4)

        for i in range(self.POP_size):
            self.parents[i] = random.choices(self.chromosomes, self.chromosomes_p)[0]
    
    def change(self, parent1, parent2):
        point = int(len(parent1)*0.5)
        cross_A = parent1[0:point]+parent2[point:]
        cross_B = parent2[0:point]+parent1[point:]
        cut_A=parent1[point:]
        cut_B=parent2[point:]
        C = [x for x in cut_A if x not in cut_B]
        D = [x for x in cut_B if x not in cut_A]
        for i in range(len(C)):
            index1 = cross_A.index(D[i], point, len(parent2))
            index2 = cross_B.index(C[i], point, len(parent1))
            cross_A[index1] = C[i]
            cross_B[index2] = D[i]
        return cross_A, cross_B

    def crossover(self):
        self.choise_parents()

        for i in range(0, self.POP_size, 2):
            self.child[i], self.child[i+1] = self.change(self.parents[i], self.parents[i+1])
    
    def mutate(self):
        for i in range(int(self.POP_size*0.8)):
            mutation = random.randint(0, self.POP_size-1)
            temp = self.child[mutation]
            s1 = random.randint(0, self.sol.numTasks-2)
            s2 = random.randint(0, self.sol.numTasks-2)
            temp[s1], temp[s2] = temp[s2], temp[s1]
            self.child[mutation] = temp
        current_best = Best_ans(self.sol, self.child)
        if self.sol.cost(current_best) < self.sol.cost(self.best):
            self.best = current_best

if __name__ == '__main__':
    with open('input.json', 'r') as inputFile:
        data = json.load(inputFile)
        for key in data:
            input = data[key]
            print('input ', key)
            solver = Problem(input)
            ans=GA(solver)
            thres = 0
            pre_best_ans = []
            i=0
            while thres!=50:
                i+=1
                ans.evaluate_fitness()
                ans.crossover()
                ans.mutate()
                #print('iteration : ', i)
                #print('ans.best', ans.best)
                if pre_best_ans == ans.best:
                    thres += 1
                else:
                    thres = 0
                pre_best_ans = ans.best
                GAans = ans.best
            print('Assignment:', GAans) # print 出分配結果
            print('Cost:', solver.cost(GAans)) # print 出 cost 是多少