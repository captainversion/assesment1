## 1.Write a program to find all pairs of an integer array whose sum is equal to a given number?

# def findPairs(lst, K):
#     res = []
#     while lst:
#         num = lst.pop()
#         diff = K - num
#         if diff in lst:
#             res.append((diff, num))
         
#     res.reverse()
#     return res
     
# lst = [1, 5, 3, 7, 9]
# K = 12
# print(findPairs(lst, K))

##----------------------------------------------------------------------------------------------------------------------------------

##2.Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

# def reverseList(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1

# A = [1, 2, 3, 4, 5, 6]
# print(A)
# reverseList(A, 0, 5)
# print("Reversed list is")
# print(A)

##----------------------------------------------------------------------------------------------------------------------------------

##3.Write a program to check if two strings are a rotation of each other?

# def areRotations(string1, string2):
#     size1 = len(string1)
#     size2 = len(string2)
#     temp = ''
 
#     if size1 != size2:
#         return 0
#     temp = string1 + string1
#     if (temp.count(string2)> 0):
#         return 1
#     else:
#         return 0
# string1 = "AACD"
# string2 = "ACDA"
 
# if areRotations(string1, string2):
#     print ("Strings are rotations of each other")
# else:
#     print ("Strings are not rotations of each other")

##-----------------------------------------------------------------------------------------------------------------------------

##4. Write a program to print the first non-repeated character from a string?

# string = "geeksforgeeks"
# index = -1
# fnc = ""
 
# if len(string) == 0 :
#   print("EMTPY STRING")
 
# for i in string:
#     if string.count(i) == 1:
#         fnc += i
#         break
#     else:
#         index += 1
# if index == len(string)-1 :
#     print("All characters are repeating ")
# else:
#     print("First non-repeating character is", fnc)
 
##--------------------------------------------------------------------------------------------------------------------------------------

 ##5.Read about the Tower of Hanoi algorithm. Write a program to implement it.

# def TowerOfHanoi(n , source, destination, auxiliary):
#     if n==1:
#         print ("Move disk 1 from source",source,"to destination",destination)
#         return
#     TowerOfHanoi(n-1, source, auxiliary, destination)
#     print ("Move disk",n,"from source",source,"to destination",destination)
#     TowerOfHanoi(n-1, auxiliary, destination, source)
         
# n = 4
# TowerOfHanoi(n,'A','B','C')

##----------------------------------------------------------------------------------------------------------------------------------

##Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# def isOperator(x):
#     if x == "+":
#         return True
#     if x == "-":
#         return True
#     if x == "/":
#         return True
#     if x == "*":
#         return True
#     return False
 
# def postToPre(post_exp):
#     s = []
#     length = len(post_exp)
#     for i in range(length):
#         if (isOperator(post_exp[i])):
#             op1 = s[-1]
#             s.pop()
#             op2 = s[-1]
#             s.pop()
#             temp = post_exp[i] + op2 + op1
#             s.append(temp)
#         else:
#             s.append(post_exp[i])
    
#     ans = ""
#     for i in s:
#         ans += i
#     return ans
 
# if __name__ == "__main__":
#     post_exp = "AB+CD-"
#     print("Prefix : ", postToPre(post_exp))

##---------------------------------------------------------------------------------------------------------------------------------

##7.Write a program to convert prefix expression to infix expression.

# def prefixToInfix(prefix):
#     stack = []
#     i = len(prefix) - 1
#     while i >= 0:
#         if not isOperator(prefix[i]):
#             stack.append(prefix[i])
#             i -= 1
#         else:
#             str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
#             stack.append(str)
#             i -= 1
#     return stack.pop()
 
# def isOperator(c):
#     if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
#         return True
#     else:
#         return False
 
# if __name__=="__main__":
#     str = "*-A/BC-/AKL"
#     print(prefixToInfix(str))
     
##-------------------------------------------------------------------------------------------------------------------------------

##8.Write a program to check if all the brackets are closed in a given code snippet.

# def check_brackets(code):
#     stack = []
#     opening_brackets = ['(', '{', '[']
#     closing_brackets = [')', '}', ']']

#     for char in code:
#         if char in opening_brackets:
#             stack.append(char)
#         elif char in closing_brackets:
#             if len(stack) == 0:
#                 return False
#             top = stack.pop()
#             if opening_brackets.index(top) != closing_brackets.index(char):
#                 return False

#     return len(stack) == 0

# # Example usage
# code = input("Enter the code snippet: ")
# if check_brackets(code):
#     print("All brackets are closed properly.")
# else:
#     print("There are unmatched brackets in the code snippet.")

##------------------------------------------------------------------------------------------------------------------------------

##9.Write a program to reverse a stack.

# class Stack:
#     def __init__(self):
#         self.Elements = []
#     def push(self, value):
#         self.Elements.append(value)
#     def pop(self):
#         return self.Elements.pop()
#     def empty(self):
#         return self.Elements == []
#     def show(self):
#         for value in reversed(self.Elements):
#             print(value)
 
# def BottomInsert(s, value):
#     if s.empty():
#         s.push(value)
#     else:
#         popped = s.pop()
#         BottomInsert(s, value)
#         s.push(popped)
 
# def Reverse(s):
#     if s.empty():
#         pass
#     else:
#         popped = s.pop()
#         Reverse(s)
#         BottomInsert(s, popped)
 
# stk = Stack() 
# stk.push(1)
# stk.push(2)
# stk.push(3)
# stk.push(4)
# stk.push(5)
 
# print("Original Stack")
# stk.show() 
# print("\nStack after Reversing")
# Reverse(stk)
# stk.show()

##-------------------------------------------------------------------------------------------------------------------------------------

##10.Write a program to find the smallest number using a stack.

# class MinStack:
#     def __init__(self):
#         self.s = []
 
#     class Node:
#         def __init__(self, val, Min):
#             self.val = val
#             self.min = Min
#     def push(self, x):
#         if not self.s:
#             self.s.append(self.Node(x, x))
#         else:
#             Min = min(self.s[-1].min, x)
#             self.s.append(self.Node(x, Min))
#     def pop(self):
#         return self.s.pop().val
#     def top(self):
#         return self.s[-1].val
#     def getMin(self):
#         return self.s[-1].min
 
# s = MinStack()
# s.push(-1)
# s.push(10)
# s.push(-4)
# s.push(0)
# print(s.getMin())
# print(s.pop())
# print(s.pop())
# print(s.getMin())
##----------------------------------------------------------------------------------------------------------------------------- 