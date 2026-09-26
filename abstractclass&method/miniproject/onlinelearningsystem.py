from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start_course(self):
        pass

class OnlineCourse(Course):
    def start_course(self):
        print(self.name, "- Online classes started")

class VideoCourse(Course):
    def start_course(self):
        print(self.name, "- Video lessons started")

class LiveCourse(Course):
    def start_course(self):
        print(self.name, "- Live classes started")

courses = [
    OnlineCourse("Python"),
    VideoCourse("Java"),
    LiveCourse("Web Development")
]

for course in courses:
    course.start_course()