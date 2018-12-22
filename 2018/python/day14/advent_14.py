

def draw(scores, elf_1, elf_2):
  output = []
  for i, score in enumerate(scores):
    if i == elf_1 and i == elf_2:
      output.append('{' + str(score) + '}')
    elif i == elf_1:
      output.append('(' + str(score) + ')')
    elif i == elf_2:
      output.append('[' + str(score) + ']')
    else:
      output.append(' ' + str(score) + ' ')
  print(''.join(output))



def solve(after):

  elf_1 = 0
  elf_2 = 1
  scores = [3, 7]

  #draw(scores, elf_1, elf_2)
  while len(scores) < after + 10:
    new_recipe = scores[elf_1] + scores[elf_2]
    if new_recipe >= 10:
      scores.append(1)
      new_recipe -= 10
    scores.append(new_recipe)
    elf_1 = (1 + elf_1 + scores[elf_1]) % len(scores)
    elf_2 = (1 + elf_2 + scores[elf_2]) % len(scores)
    
    #draw(scores, elf_1, elf_2)

  return ''.join(str(i) for i in scores[after:(after+10)])

def try_goal(goal, scores):
  if len(scores) < len(goal): return False
  for i in xrange(len(goal)):
    if scores[-(i+1)] != goal[len(goal)-i-1]:
      return False
  return True

def solve_part_2(goal_str):

  goal = list(int(c) for c in goal_str)

  elf_1 = 0
  elf_2 = 1
  scores = [3, 7]

  #draw(scores, elf_1, elf_2)
  while True:
    new_recipe = scores[elf_1] + scores[elf_2]
    if new_recipe >= 10:
      scores.append(1)
      if try_goal(goal, scores): return len(scores) - len(goal)
      new_recipe -= 10
    scores.append(new_recipe)
    if try_goal(goal, scores): return len(scores) - len(goal)
    elf_1 = (1 + elf_1 + scores[elf_1]) % len(scores)
    elf_2 = (1 + elf_2 + scores[elf_2]) % len(scores)
    
    #draw(scores, elf_1, elf_2)
    #print(goal)


# print(5, '0124515891', solve(5))
# print(18, '9251071085', solve(18))
# print(2018, '5941429882', solve(2018))
# print(509671, '2810862211', solve(509671))


print('51589', 9, solve_part_2('51589'))
print('01245', 5, solve_part_2('01245'))
print('92510', 18, solve_part_2('92510'))
print('59414', 2018, solve_part_2('59414'))
print('509671', '?', solve_part_2('509671'))


