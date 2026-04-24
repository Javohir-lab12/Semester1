class ExamError(Exception):
    pass

class StudentAlreadyRegisteredError(ExamError):
    def __init__(self, name):
        self.name = name
        super().__init__(f"student already registered: {name}")

class StudentNotRegisteredError(ExamError):
    def __init__(self, name):
        self.name = name
        super().__init__(f"student not registered: {name}")

class InvalidAnswerError(ExamError):
    def __init__(self, question_num, valid_options):
        self.question_num = question_num
        self.valid_options = valid_options
        super().__init__(f"invalid answer for question {question_num}. valid options: {valid_options}")

class ExamGrader:
    def __init__(self, answer_key: dict[int, str]):
        self.answer_key = answer_key
        self.student_submission: dict[str, dict[int, str] | dict] = {}
    def register_student(self, name):
        if name in self.student_submission:
            raise StudentAlreadyRegisteredError(name)
        self.student_submission[name] = {}
    def submit_answer(self, name, question_num, answer):
        try:
            submission = self.student_submission[name] 
        except KeyError:
            raise StudentNotRegisteredError(name) from None
        if question_num not in self.answer_key:
            raise InvalidAnswerError(question_num, list(self.answer_key.keys()))
        submission[question_num] = answer
    def grade(self, name):
        try:
            student = self.student_submission[name]
        except KeyError:
            raise StudentNotRegisteredError(name) from None
        if not student:
            return 0
        total_number_of_correct_answers = len([(num, answer) for num, answer in student.items() if self.answer_key[num] == answer])
        return int(total_number_of_correct_answers / len(self.answer_key) * 100)

key = {1: "B", 2: "A", 3: "C", 4: "D"}
grader = ExamGrader(key)

grader.register_student("Dana")
grader.register_student("Emir")

grader.submit_answer("Dana", 1, "B")
grader.submit_answer("Dana", 2, "A")
grader.submit_answer("Dana", 3, "B")
grader.submit_answer("Dana", 4, "D")

grader.submit_answer("Emir", 1, "B")
grader.submit_answer("Emir", 2, "C")

print(f"Dana: {grader.grade('Dana')}%")
print(f"Emir: {grader.grade('Emir')}%")

tests = [
    lambda: grader.register_student("Dana"),
    lambda: grader.submit_answer("Zara", 1, "A"),
    lambda: grader.submit_answer("Emir", 7, "A"),
]

for test in tests:
    try:
        test()
    except ExamError as e:
        print(e)