# 小程式紀錄
- arithmetic.py:
  - 計算四則運算
  - 可以用的符號：+, -, *, /, ^, %
  - 會先計算括弧內的答案
```ruby
from arithmetic import calculator
# example
x1 = "2*9*3+5*8/2+60%10/5/3+0.212"
x2 = "(((2*9*3+5*8)/2+6*(4^5))/2+(12-23))*3"
x3 = "2*(5-1)+(((2*9*3+5*8)/2+6*(4^5))/2+(12-23))*3"
x4 = "10/3"

print(calculator(x1))  #74.212
print(calculator(x2))  #9253.5
print(calculator(x3))  #9261.5
print(calculator(x4))  #3.3333333333333335
```
- knight_tour.py:
  - Problems: A Solution for Knight’s Tour with NxN Chessboard (8 ≤ N ≤ 30)
  - Note: If N is an odd number, there exist the solutions only for Knight’s start positions at (i, j) where the sum of i and j is equal to
    an even number.
  - Solution Steps:
    1. Creating a degree map for an 8x8 chessboard.
    2. Creating the 8 possible moves.
    3. Initiating the **start position** of Knight.
    4. Looping for finding the Hamiltonian Path for Knight’s Tour.
      - Checking if the moves within the board boundaries or not.
      - Finding the next position for Knight's movement.
      - Updating the degree map and the new move.
    5. Print out the Hamiltonian Path for Knight’s Tour
```ruby  
from knight_tour import knight_tour
tour = knight_tour(8,4,5)
if tour != "knight tour not found":
    for i in range(len(tour)):
            for j in range(len(tour)):
                print("{:3d}".format(tour[i][j]), end =" ")
            print()
else:
    print(tour)
```
