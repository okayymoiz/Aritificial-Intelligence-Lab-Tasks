class ClassroomAgent:
 def __init__(self):
  self.previous_mode = "None"
 def act(self, temp, occupied):
  if not occupied:
   current_mode= "ECO"
  elif temp > 26:
   current_mode= "COOL"
  elif temp < 20:
   current_mode= "WARM"
  else:
   current_mode= "IDLE"

  if current_mode == self.previous_mode:
   command = "No Command for Update"
  else:
   command = "Update!!"

  old_mode = self.previous_mode
  self.previous_mode = current_mode

  return old_mode , command , self.previous_mode
  
agent = ClassroomAgent()
percepts = [(29, True), (29, True), (20, True),
 (26, True), (19, True), (29, False)]
for step, percept in enumerate(percepts, 1):
 print(step, percept, "target mode", agent.act(*percept))
