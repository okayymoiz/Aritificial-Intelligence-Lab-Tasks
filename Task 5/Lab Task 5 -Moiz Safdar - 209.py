import math
print("Question no 2 ")
def minimax(curDepth,nodeIndex,maxTurn,scores,targetDepth, count):

    if curDepth == targetDepth:
        count[0] += 1
        return scores[nodeIndex]
    if maxTurn:
        return max(
            minimax(curDepth +1,nodeIndex *2, False,scores, targetDepth,count),
            minimax(curDepth +1,nodeIndex *2 + 1,False, scores,targetDepth, count)
        )
    else:
        return min(
            minimax(curDepth +1,nodeIndex *2,True, scores,targetDepth, count),
            minimax(curDepth +1,nodeIndex *2 + 1,True,scores,targetDepth,count)
        )

def alphabeta(depth,index,maxTurn,scores,target,alpha,beta, count):
    if depth == target:
        count[0] += 1
        return scores[index]
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(depth + 1, index *2 + i,False,scores,target,alpha,beta,count))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(depth +1, index *2 + i,True,scores,target, alpha,beta, count))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

scores = [3, 5, 2, 9, 3, 5, 2, 9]
treeDepth = int(math.log2(len(scores)))

# Minimax
count = [0]
result = minimax(0, 0, True, scores, treeDepth, count)

print("Minimax final value:", result)
print("Minimax leaves counter:", count[0])

# AlphaBeta
count = [0]
result = alphabeta(0, 0, True, scores, treeDepth, float('-inf'), float('inf'), count)

print("AlphaBeta final value:", result)
print("AlphaBeta leaves counter:", count[0])

#  ----- Q3 part ----- 

print("\n Question no 3 ")

reordered_scores = [3, 5, 2, 9, 2,9, 3, 5]
treeDepth = int(math.log2(len(reordered_scores)))

# Minimax
count = [0]
result = minimax(0, 0, True,reordered_scores, treeDepth, count)
print("Minimax final value:", result)
print("Minimax leaves counter:", count[0])

# AlphaBeta
count = [0]
result = alphabeta(0, 0, True, reordered_scores, treeDepth, float('-inf'), float('inf'), count)
print("AlphaBeta final value:", result)
print("AlphaBeta leaves counter:", count[0])