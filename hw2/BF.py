class Problem:
    def __init__(self, input):
        self.input = input
        self.numTasks = len(input)
    def cost(self, ans):
        totalTime = 0
        for task, agent in enumerate(ans):
            totalTime += self.input[task][agent]
        return totalTime

###########################
# your algorithm class
###########################

def permutations(start, end=[], result=[]):
    if len(start) == 0:
        result.append(list(end))
    else:
        for i in range(len(start)):
            permutations(start[:i] + start[i+1:], end + start[i:i+1])
    return result

def BF(numAgents):
    result = permutations(list(range(numAgents)))

    min = solver.cost(result[0])
    index = 0
    for i in range(len(result)):
        cost = 0
        for task, agent in enumerate(result[i]):
            cost+=input[task][agent]
        if cost<min : 
            index = i
            min = cost
    return result[index]
    

if __name__ == '__main__':
    input = [
    [0.71773280, 0.28980792, 0.86571783, 0.44026587, 0.53155829],
    [0.30556295, 0.56751479, 0.75442822, 0.62446877, 0.30992529],
    [0.83717620, 0.52213939, 0.54137934, 0.15001555, 0.70178034],
    [0.53279199, 0.08006661, 0.70693305, 0.29315974, 0.69018493],
    [0.03981310, 0.25511235, 0.94795653, 0.41611858, 0.50587076]
    ]
    solver = Problem(input)
    numAgents = len(input[0])
    BFans = BF(numAgents)

    #yourAssignment = [3, 2, 0, 1] #⽤演算法得出的答案
    #solver = Problem(input)
    print('Assignment:', BFans) # print 出分配結果
    print('Cost:', solver.cost(BFans)) # print 出 cost 是多少
