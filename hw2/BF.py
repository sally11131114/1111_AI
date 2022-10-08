import json
import math
from unittest import result

from matplotlib.pyplot import flag
class Problem:
    def __init__(self, input):
        self.input = input
        self.numTasks = len(input)
    def cost(self, ans):
        totalTime = 0
        for task, agent in enumerate(ans):
            totalTime += self.input[task][agent]
        return totalTime
result=[]
def permutations(input, num, end=[]):
    global result
    in_len=len(input)
    # if flag==1:
    #     result=[]
    #     flag=0
    if in_len == 0:
        result.append(list(end))
        #print('result:', result)
        # if len(result) == math.factorial(num):
        #     print('len(result): ', len(result))
        #     print('math.factorial(global_num)', math.factorial(num))
        #     print('result: ', result)
        #     return result
    else:
        for i in range(in_len):
            permutations(input = input[:i] + input[i+1:], num=num, end= end + input[i:i+1])

def BF(solver):
    global result
    #print('numAgents:', solver.numTasks)
    # global_num = solver.numTasks
    # print('global_num: ', global_num)
    #result=[]
    permutations(list(range(solver.numTasks)), num=solver.numTasks)
    #print('####', result)

    # if result>math.factorial(solver.numTasks):
    #     result = result[]
    # if solver.numTasks==4:
    #     print(result)
    min = solver.cost(result[0])
    index = 0
    for i in range(len(result)):
        tmp_cost = solver.cost(result[i])
        if tmp_cost<min : 
            index = i
            min = tmp_cost
    return result[index]

    # result = permutations(list(range(numAgents)))

    # min = solver.cost(result[0])
    # index = 0
    # for i in range(len(result)):
    #     cost = 0
    #     for task, agent in enumerate(result[i]):
    #         cost+=input[task][agent]
    #     if cost<min : 
    #         index = i
    #         min = cost
    # return result[index]
    

if __name__ == '__main__':
    with open('input.json', 'r') as inputFile:
        data = json.load(inputFile)
        for key in data:
            input = data[key]
            print('input ', key)
            solver = Problem(input)
            BFans = BF(solver)
            print('Assignment:', BFans) # print 出分配結果
            print('Cost:', solver.cost(BFans)) # print 出 cost 是多少
            result.clear()
