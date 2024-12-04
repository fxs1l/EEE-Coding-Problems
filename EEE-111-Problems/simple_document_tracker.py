class Document:
  #TO DO: define the constructor method, __init__ and then initialize values
  def __init__(self, initial_thoughts=""):
    if len(initial_thoughts) == 0:
        self.word_count = 0
    else:
        self.word_count = len(initial_thoughts.split())
    self.status = "draft"
    self.grade = "awaiting submission"
    self.asked_grade_before_submission_count  = 0

  #TO DO: define the method add_words
  def add_words(self, additional_thoughts):
    if len(additional_thoughts) <= 1000:
        self.word_count += len(additional_thoughts.split())
  
  
  #TO DO: define the method submit
  def submit(self):
    self.status = "submitted"
    self.grade = "awaiting request"

  #TO DO: define the method get_grade
  def get_grade(self):
    self.grade = "A+"
    if self.status != "submitted":
        self.asked_grade_before_submission_count += 1
        
  def __str__(self):
    #TO DO: Fill in the blanks
    document_info = f"This Document instance has 4 instance attributes.\n"
    document_info += f"The class used to create this object has 5 methods and 0 class attributes.\n"
    document_info += f"This Document instance has the following stats.\n"
    #TO DO: Complete document_info by adding more lines below
    document_info += f"1. word count: {self.word_count}\n"
    document_info += f"2. status: {self.status}\n"
    document_info += f"3. grade: {self.grade}\n"
    document_info += f"4. number of times the grade was requested before the document was submitted: {self.asked_grade_before_submission_count}"
    return document_info
  
if __name__ == "__main__":
  while(True):
    command = input()
    if command == 'exit':
      break
    exec(command)
  print(essay)
