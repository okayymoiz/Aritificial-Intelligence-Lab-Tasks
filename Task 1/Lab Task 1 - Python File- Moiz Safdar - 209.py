def rule_based(score, documents_complete,attendance,conduct):
 return "Review" if  score >= 70 and documents_complete and attendance >= 75 and conduct else "Hold"

cases = [
 ("Pass",82, True, 90, True,"Review","All Conditions are true and Satisfied"),
 ("Attendendance Faliure ", 68, True, 70,True,"Hold","Student is Below Required Attendance"),
 ("Conduct Faliure", 91, True,92,False,"Hold","There is an Issue with Student Conduct"),
 ("Threshold boundary", 70, True, 75,True,"Review","Conditions meets threshold")]

for name, score, complete,attendance, conduct, expected_output,reason in cases:
  a = rule_based(score, complete, attendance,conduct)
  print(f"\n Case: {name}")
  print(f"Input:  Score : {score} | Document Complete : {complete} | Attendence : {attendance} | Conduct : {conduct} " )
  print(f"Expected Result : {expected_output}")
  print(f"Actual Result : {a} ")
  print(f"Reason : {reason} ")
