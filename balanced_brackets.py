#Balanced Brackets
# Write a function that takes in a string made up of brackets ((,[,{,],),}) and other optional characters. The function should return a boolean representing whether the string is balanced with regards to brackets. 

#A string is said to be balanced if it has as many opening brackets of a certain type as it has closing brackets of that type and if no bracket is unmatched. Note that an opening bracket cant match a corresponging closing brakcet that comes before it, and similarly, a  closing bracket cant martch a corresponding opening bracket that comes after it. Also, brakcets cant overlap each other as in [(]).

#Sample input, string = "([])(){}(())()()"
#Sample output, true // it's balanced

def balancedBrackets(string):
    pass
print(balancedBrackets("([])(){}(())()()"))