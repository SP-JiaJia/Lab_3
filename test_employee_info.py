import employee_info

def test_get_employees_by_age_range():
    result = []
    test = [
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]

    #employees whose age are more than 35 and less than 50
    result = employee_info.get_employees_by_age_range(35, 50)
    
    assert(result == test)

def test_calculate_average_salary():
    result = 0
    test = 60166.67

    result = employee_info.calculate_average_salary()

    assert(result==test)

def test_get_employees_by_dept():
    result = []
    test=[
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]

    result=employee_info.get_employees_by_dept("engineering")

    assert(result==test)