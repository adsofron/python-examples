grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  sum = 0
  for i in range(len(scores)):
    sum +=scores[i]
  print(sum)

grades_sum(grades)
