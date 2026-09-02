from src.intern_class import Intern
from src.profile import print_profile

intern = Intern(
    "Rohit Raj Singh",
    "Software Engineering Intern",
    "Software Development",
    ["Python", "Django", "Git", "SQL", "Cloud"]
)

intern.print_profile()


#to run python3 -m tests.test_intern_class