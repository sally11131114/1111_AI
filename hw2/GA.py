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
        self.POP_size = 80#int(fact(solver.numTasks)/10)
        self.chromosomes = [[ j  for j in range(solver.numTasks)] for i in range(self.POP_size)]
        self.chromosomes_cost = [ 0 for i in range(self.POP_size)]
        self.chromosomes_fitness = [ 0 for i in range(self.POP_size)]
        self.chromosomes_p = [ 0 for i in range(self.POP_size)]
        self.parents = [ 0 for i in range(self.POP_size)]
        self.child = [ 0 for i in range(self.POP_size)]
        self.best = []
        self.sol = solver

        # while True :
        #     self.chromosomes_dup = [ 0 for i in range(self.POP_size)]
        #     for i in range(self.POP_size):
        #         random.shuffle(self.chromosomes[i])
        #         for j in range(solver.numTasks):
        #             self.chromosomes_dup[i] += self.chromosomes[i][j]*pow(10, j)
        #     print('len : ', len(set(self.chromosomes_dup)))
        #     if len(set(self.chromosomes_dup)) == self.POP_size : break; 
        #     #檢查染色體有沒有重複 

        for i in range(self.POP_size):
            random.shuffle(self.chromosomes[i])
        #檢查染色體有沒有重複 

        self.best = Best_ans(self.sol, self.chromosomes)
        print('After shuffle : ', self.chromosomes)
        print('self.best: ', self.best)

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
            print(self.parents[i])
        print('parent = ', len(self.parents))
    
    def change(self, parent1, parent2):
        # print('A : ', parent1)
        # print('B : ', parent2)
        point = int(len(parent1)/2)
        # print('point: ', point) #3
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

        for i in range(0, self.POP_size, 2):
            self.child[i], self.child[i+1] = self.change(self.parents[i], self.parents[i+1])
        print('child : ', self.child)
    
    def mutate(self):
        for i in range(int(self.POP_size/3)):
            mutation = random.randint(0, self.POP_size-1)
            print('mutation', mutation)
            temp = self.child[mutation]
            s1 = random.randint(0, self.sol.numTasks-1)
            s2 = random.randint(0, self.sol.numTasks-1)
            print('s1, s2: ', s1, s2)
            temp[s1], temp[s2] = temp[s2], temp[s1]
            self.child[mutation] = temp
            #print("HI", int(POP_size/3))
        print('child after mutate: ', self.child)
        current_best = Best_ans(self.sol, self.child)
        if self.sol.cost(current_best) < self.sol.cost(self.best):
            self.best = current_best
        print('self.best: ', self.best)

if __name__ == '__main__':
    input = [
    [0.43045255, 0.78681387, 0.07514408, 0.72583933, 0.52916145, 0.87483212, 0.34701621],
 [0.68704291, 0.45392742, 0.46862110, 0.67669006, 0.23817468, 0.87520581, 0.67311418],
 [0.38505150, 0.05974168, 0.11388629, 0.28978058, 0.66089373, 0.92592403, 0.70718757],
 [0.24975701, 0.16937649, 0.42003672, 0.88231235, 0.74635725, 0.59854858, 0.88631100],
 [0.64895582, 0.58909596, 0.99772334, 0.85522575, 0.33916707, 0.72873479, 0.26826203],
 [0.47939038, 0.88484586, 0.05122520, 0.83527995, 0.37219939, 0.20375257, 0.50482283],
 [0.58926554, 0.45176739, 0.25217475, 0.83548120, 0.41687026, 0.00293049, 0.23939052]
    ]
    solver = Problem(input)
    ans=GA(solver)
    thres = 0
    pre_best_ans = []
    # while thres!=5:
    #     ans.evaluate_fitness()
    #     ans.crossover()
    #     ans.mutate()
    #     print('pre_best_ans: ', pre_best_ans)
    #     print('ans.best', ans.best)
    #     if pre_best_ans == ans.best:
    #         thres += 1
    #         print('HHHHHEY')
    #     else:
    #         thres = 0
    #     print('thres: ', thres)
    #     pre_best_ans = ans.best
    for i in range(150):
        ans.evaluate_fitness()
        ans.crossover()
        ans.mutate()
    GAans = ans.best
    print('Assignment:', GAans) # print 出分配結果
    print('Cost:', solver.cost(GAans)) # print 出 cost 是多少