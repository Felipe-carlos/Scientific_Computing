import re
#creates a funtion to print the string like a matrix
def prints(string):
  p_line = []
  max_len =len(max(string, key=len))
  p_line.append(string[0].rjust(max_len+2)) 
  p_line.append(string[1] + " " + string[2].rjust(max_len))
  p_line.append("-" * (max_len+2))
  return p_line
  
def pretty_answer(only_string):
  if len(only_string) > 5:
     return "Error: Too many problems."
  else:
    error = 0
    splited_calc = []
    #splits the data and verifies it
    for num,string in enumerate(only_string):    
      splited_calc.append(string.split(" ")) 
      if splited_calc[num][1] != '+' and splited_calc[num][1] != '-': 
              arranged_problems = "Error: Operator must be '+' or '-'."  
              error = 1
      if not splited_calc[num][0].isdigit() or not splited_calc[num][2].isdigit():
        arranged_problems = "Error: Numbers must only contain digits."
        error = 1
      if len(re.findall(r'\d', splited_calc[num][0])) > 4 or len(re.findall(r'\d', splited_calc[num][2])) > 4 : 
        arranged_problems = 'Error: Numbers cannot be more than four digits.'
        error = 1
    if error == 0:
      p_prints = []
      final = []
      for i in splited_calc:
        p_prints.append(prints(i))
      for j in range(3):
        final.append([linha[j] for linha in p_prints])

      arranged_problems = "    ".join(final[0]) + "\n" + "    ".join(final[1]) + "\n" +"    ".join(final[2])
    return arranged_problems
  
def arithmetic_arranger(problems,flag=None):
  if type(flag) == bool:
    if flag == True:
      operation = pretty_answer(problems) 
      if operation.count('\n') >1:
        splited_calc = []
        value = []
        sizes = []
        for num,string in enumerate(problems):    
          splited_calc.append(string.split(" "))
          sizes.append(len(max(splited_calc[num], key=len)))
          if splited_calc[num][1] == "+":
            value.append(str(int(splited_calc[num][0])+int(splited_calc[num][2])).rjust(sizes[num]+2))
          else: 
            value.append(str(int(splited_calc[num][0])-int(splited_calc[num][2])).rjust(sizes[num]+2))
            
        final = operation  +"\n"+ "    ".join(value)
        
        return final
      else:
        return operation
    else:
      return pretty_answer(problems)
  else:
    return pretty_answer(problems)