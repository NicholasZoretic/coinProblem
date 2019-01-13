import math
'''
creates a nested loop with recursion
tests all possible combinations of values to see if it is possible to make the number input with values given
'''
def isCoin(listnums, num, sumn, x): 
    maxn = int(num/listnums[x]) + 1 #range of values tested for coin x in listnums
    for i in range(0,maxn):
        temp = list(sumn)
        temp.append(listnums[x] * i) #adds value of coin * quantity to sum
        #print(str(num) + '=' + str(sum(temp)))
        if(sum(temp) == num): #if current value satisfies number, return true
            return True
        elif(x + 1 != len(listnums) and isCoin(listnums, num, temp, x+1)): #tests next level down for a solution
            return True
    return False #if no combination of values is found to satisfy

'''
loops thru range
returns list of all values which cannot be created by the list of coins
'''
def allNonCoins(listn, maxn):
    final = [] #list returned
    for i in range(0,maxn + 1): #loops thru range requested
          if not (isCoin(listn, i, [], 0)): #if it is not a coin, add to the list
              final.append(i)
    return final
'''
I know that the largest non coin value for a large set of values must be smaller than that of a subset of those values
Only works if two numbers gcd is one
'''
def listNonCoin(listn): 
    final = []
    listn.sort()
    for i in range(len(listn)):
        for j in range(i + 1, len(listn)):
            if math.gcd(listn[i],listn[j]) == 1:
                final.append((listn[i] - 1) * (listn[j] - 1) - 1)
    if final==[]:
        print('infinity')
        return
    final.sort()
    return allNonCoins(listn, final[0] + 1)

def largestNonCoin(listn): 
    nonc = listNonCoin(listn)
    return nonc[len(nonc) - 1]

def numNonCoin(listn):
    nonc = listNonCoin(listn)
    return len(nonc)

a = []
while(1==1):
  l = int(input('enter multiple coins, -1 to finish list: '))
  if(l == -1):
    break
  a.append(l)

print('largest number not possible:')
print(largestNonCoin(a))

print('number of not possible coin combos:')
print(numNonCoin(a))

print('list of coin combinations not possible:')
print(listNonCoin(a))
