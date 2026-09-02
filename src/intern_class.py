class Intern:

    def __init__(self, name, role, department, skills):
        self.name = name
        self.role = role
        self.department = department
        self.skills = skills

    def print_profile(self):
        print("Intern Name:", self.name)
        print("Role:", self.role)
        print("Department:", self.department)
        print("Skills:", ", ".join(self.skills))