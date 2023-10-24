import random
comments=["You have shown a keen interest in discussing economic issues in class.",
  "Your written work has been quite meticulous with effective use of economic terminology.",
  "You have demonstrated a solid understanding of economic concepts at this level.",
  "You have worked hard in economics this semester and it shows in your grades.",
  "You have shown great improvement in your understanding of economic concepts since the beginning of the semester.",
  "You could benefit from participating more in class discussions to deepen your understanding of economic concepts.",
  "You could improve your written work by paying closer attention to detail and using more economic terminology.",
  "You could benefit from reviewing economic concepts more regularly to reinforce your understanding.",
  "You could improve your grades by seeking extra help outside of class when you are struggling with economic concepts.",
  "You could benefit from practicing more economic problems to improve your problem-solving skills."]
NumberOfStudents = 20
for x in range(NumberOfStudents):
  print(comments[random.randint(0,len(comments)-1)])
