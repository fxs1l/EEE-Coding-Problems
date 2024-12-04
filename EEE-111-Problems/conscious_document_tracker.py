classes = {}

class Document:
    key = 0
    #TO DO: place attributes and methods from the previous exercise here
    def __init__(self, initial_thoughts=""):
        if len(initial_thoughts) > 0:
            self.word_count = len(initial_thoughts.split())
        self.status = "draft"
        self.grade = "awaiting submission"
        self.asked_grade_before_submission_count  = 0
        
    def add_words(self, additional_thoughts):
        if len(additional_thoughts) <= 1000:
            self.word_count += len(additional_thoughts.split())
            
    def submit(self):
        self.status = "submitted"
        self.grade = "awaiting request"
        
    def get_grade(self):
        self.grade = "A+"
        if self.status != "submitted":
            self.asked_grade_before_submission_count += 1
    #TO DO: add new attributes and methods here
    def copy_content(self, source_document):
        self.word_count = source_document.word_count
        return self
    def append_content(self, source_document):
        self.word_count += source_document.word_count
        return self
    
    def __str__(self):
        document_info = f"This Document instance has the following stats.\n"
        document_info += f"1. word count: {self.word_count}\n"
        document_info += f"2. status: {self.status}\n"
        document_info += f"3. grade: {self.grade}\n"
        document_info += f"4. number of times the grade was requested before the document was submitted: {self.asked_grade_before_submission_count}\n"
        
        #TO DO: Fill in the blanks
        if self.key <= 3:
            document_info += ""
        elif self.key == 4:
            document_info += f"This Document instance has 4 instance attribute/s."
        elif self.key == 5:
            document_info += f"The class used to create this object has 7 method/s."
        elif self.key == 6:
            document_info += f"The class used to create this object has 1 class attribute/s."
        elif self.key == 7:
            document_info += f"The class used to create this object has 2 special method/s."
        return document_info

def is_command_valid(command):
    global classes
    #TO DO: add validation steps here
    if len(command.split(".")) < 2: # probably not a dot expression? 
         return False
    doc_key = command.split(".")[0]
    # Not a valid document
    if doc_key not in classes:
        return False
    document = classes.get(doc_key)
    names = command.split(".")[1:]
    for i in range(len(names)):
        attribute = names[i].split("(")[0]
        if not hasattr(document, attribute):
            return False
        else:
            if len(names[i].split("(")) > 1: #is a method  
                if 0 < i < len(names) and "_content" not in names[i-1]:
                    return False
        names[i] = attribute
    return True
  
if __name__ == "__main__":
    while(True):
        command = input()
        if command == 'exit':
            break
        elif command.find(" = ") != -1:
            exec(command)
            print("Valid command")
        else:
            if is_command_valid(command):
                exec(command)
                print("Valid command")
            else:
                print("Invalid command")
    print(essay)
