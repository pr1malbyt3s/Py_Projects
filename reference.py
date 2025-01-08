def for_loop():
  for i in range(0, 100): # This is first number inclusive, second number exclusive. This example is 0-99. https://www.w3schools.com/python/ref_func_range.asp
    if(i != 27):
      continue # Continue goes back to loop start and skips rest of loop statements. https://www.learnpython.dev/02-introduction-to-python/110-control-statements-looping/40-break-continue/
    print(i)
    if(i == 27):
      break # Break statements break completely out of the loop and would not run iterate anymore. https://www.learnpython.dev/02-introduction-to-python/110-control-statements-looping/40-break-continue/.
  return # Immediately exits a function
