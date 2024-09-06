test_scores = [61, 31, 30, 51, 36, 46, 72, 46, 53, 52, 50, 67, 39, 41, 54, 61, 57, 74, 45, 3, 49, 76, 67, 41, 41, 47, 45, 57, 44, 0, 35, 41, 51, 63, 56, 31, 70, 44, 54, 73, 47, 48, 66, 22, 57, 75, 86, 35, 38, 31]

test_participants = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah", "Ian", "Jane", "Kevin", "Laura", "Michael", "Nina", "Oliver", "Paula", "Quincy", "Rachel", "Samuel", "Tina", "Uma", "Victor", "Wendy", "Xavier", "Yvonne", "Zachary", "Adam", "Beth", "Carl", "Daisy", "Ethan", "Faith", "Gavin", "Helen", "Isaac", "Julia", "Kyle", "Lily", "Martin", "Nora", "Oscar", "Penelope", "Quinn", "Ruth", "Scott", "Tracy", "Ursula", "Vincent", "Willow", "Xander"] 

for i in range(1,len(test_scores)):
  if test_scores[i] <= 40:
    print(str(test_participants[i]) +"\t"+ str(test_scores[i]))
