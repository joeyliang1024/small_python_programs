# 小程式紀錄
- calculator.py:
  - 計算四則運算
  - 可以用的符號：+, -, *, /, ^, %
  - 會先計算括弧內的答案
  - ```ruby
from arithmetic import calculator

x1 = "2*9*3+5*8/2+60%10/5/3+0.212"
x2 = "(((2*9*3+5*8)/2+6*(4^5))/2+(12-23))*3"
x3 = "2*(5-1)+(((2*9*3+5*8)/2+6*(4^5))/2+(12-23))*3"
x4 = "10/3"

print(calculator(x1)) 
print(calculator(x2))  
print(calculator(x3))  
print(calculator(x4))
```
