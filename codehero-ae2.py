test_scores = [61, 31, 30, 51, 36, 46, 72, 46, 53, 52, 50, 67, 39, 41, 54, 61, 57, 74, 45, 3, 49, 76, 67, 41, 41, 47, 45, 57, 44, 0, 35, 41, 51, 63, 56, 31, 70, 44, 54, 73, 47, 48, 67, 22, 57, 75, 86, 35, 38, 31]

test_participants = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah", "Ian", "Jane", "Kevin", "Laura", "Michael", "Nina", "Oliver", "Paula", "Quincy", "Rachel", "Samuel", "Tina", "Uma", "Victor", "Wendy", "Xavier", "Yvonne", "Zachary", "Adam", "Beth", "Carl", "Daisy", "Ethan", "Faith", "Gavin", "Helen", "Isaac", "Julia", "Kyle", "Lily", "Martin", "Nora", "Oscar", "Penelope", "Quinn", "Ruth", "Scott", "Tracy", "Ursula", "Vincent", "Willow", "Xander"] 
first = 0
second = 0
third = 0
for i in range(1,50):
  if test_scores[i] >= first:
    first=test_scores[i]
  elif test_scores[i] >= second:
    second=test_scores[i]
  elif test_scores[i] >= third:
    third=test_scores[i]
print("1st place:"+str(first))
print("second place:"+str(second))
print("third place:"+str(third))
