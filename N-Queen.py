n=int(input("Enter a value:"))

def solve_nqueens(i,ans):
  if i==n:
    solutions.append(ans[:])
    return
  for j in range(n):
    if is_safe(ans,i,j):
      ans.append(j)
      solve_nqueens(i+1,ans)
      ans.pop()
        
def is_safe(ans,i,j):
  for k in range(i):
    if ans[k]==j or abs(ans[k]-j)==abs(k-i):
      return False
  return True

def display(solutions):
    print("The solutions are:")
    l=1
    for sol in solutions:
        print(f"Solution {l}:")
        l+=1
        for i in range(n):
            for j in range(n):
                if j == sol[i]:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

solutions=[]
solve_nqueens(0,[])
if(solutions):
  display(solutions)
else:
  print("No solution")


# Sample output for n=4
# The solutions are:
# Solution 1:
# . Q . . 
# . . . Q 
# Q . . . 
# . . Q . 
# 
# Solution 2:
# . . Q . 
# Q . . . 
# . . . Q 
# . Q . . 
