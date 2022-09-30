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
    def __init__(self, numTasks):
        self.chromosomes = [[ j  for j in range(numTasks)] for i in range(POP_size)]
        self.chromosomes_dup = [ 0 for i in range(POP_size)]
        
        while True :
            for i in range(POP_size):
                random.shuffle(self.chromosomes[i])
                for j in range(numTasks):
                    self.chromosomes_dup[i] += self.chromosomes[i][j]*pow(10, j)
            if len(set(self.chromosomes_dup)) == POP_size : break; 
            #檢查染色體有沒有重複 
        print('After shuffle : ', self.chromosomes)

if __name__ == '__main__':
    input = [
    [10, 20, 23,  4],
    [15, 13,  6, 25],
    [ 2, 22, 35, 34],
    [12,  3, 14, 17]
    ]
    solver = Problem(input)
    GA(solver.numTasks)

    #numAgents = len(input[0])
    #BFans = BF(numAgents)

    #yourAssignment = [3, 2, 0, 1] #⽤演算法得出的答案
    #solver = Problem(input)
    #print('Assignment:', BFans) # print 出分配結果
    #print('Cost:', solver.cost(BFans)) # print 出 cost 是多少