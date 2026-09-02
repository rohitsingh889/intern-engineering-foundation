from src.profile import intern_name, role, department, skills


def test_profile_data():
    assert intern_name == "Rohit Raj Singh"
    assert role == "Software Engineering Intern"
    assert department == "Software Development"
    assert "Python" in skills
    assert "Git" in skills
    assert "Cloud" in skills


test_profile_data()
#python3 -m tests.test_profile to run the test