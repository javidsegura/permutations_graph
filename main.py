from itertools import permutations 
import random, time
import matplotlib.pyplot as plt

t0 = time.time() # Start timer

def func(x): # x will be a sequence
      results = []
      k = []
      for i in range(8): # Modify x three times
            x.append(random.randint(1, 9)) # Modify the list by adding a random number to the end
            z = list(permutations(x, len(x))) # Make all possible x-pairs for x
            results.append(z) # Append the permutations of each iteration to results
      for i in results:
            k.append(len(i)) # Get the lenght of each iteration
      return k


results = func([1, 2, 3]) #Introuce a default sequence
t1 = time.time() # Finish timer
print("List with lenght of each permutation is: ", results,"\n","-"*60, f"\nTotal runtime: {round(t1-t0,2)} seconds \n","-"*60)

# Start plotting
k = results 
plt.plot(k)
plt.xlabel('Iteration')
plt.ylabel('Length of x in tens of millions')
plt.title('Plot of x')
plt.show()
