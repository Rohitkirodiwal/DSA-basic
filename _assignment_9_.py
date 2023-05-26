def reverse_stack(str):

  stack = []                         # Create an empty stack (list to use as stack)
   # Push all characters of string to stack
  for char in str:
      stack.append(char)

  rev = ''
  while len(stack) > 0:
       last = stack.pop()           # Pop all characters of string  and add it to the rev
       rev = rev + last
             
  return rev

user_str = input("Enter your string : ")
reverse = reverse_stack(user_str)
print('Reversed is: ', reverse)