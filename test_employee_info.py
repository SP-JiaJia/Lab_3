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

    expected_result_engineering=[
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    result=employee_info.get_employees_by_dept("engineering")
    assert(result==expected_result_engineering)

    expected_result_Engineering=[
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    result=employee_info.get_employees_by_dept("Engineering")
    assert(result==expected_result_Engineering)

    expected_result_sales=[
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    result=employee_info.get_employees_by_dept("sales")
    assert(result==expected_result_sales)

    expected_result_Sales=[
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    result=employee_info.get_employees_by_dept("Sales")
    assert(result==expected_result_Sales)

    expected_result_marketing=[
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    result=employee_info.get_employees_by_dept("marketing")
    assert(result==expected_result_marketing)
    
    expected_result_Marketing=[
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    result=employee_info.get_employees_by_dept("Marketing")
    assert(result==expected_result_Marketing)