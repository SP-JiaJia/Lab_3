import Lab_2.bmi as bmi

print("Test_Lab2_bmi.py")

def test_bmi_normal_weight():
    result = 0
    input_height = 1.78
    input_weight = 66
    test_bmi = 0 #"0" for normal weight

    result = bmi.calculate_bmi(input_height,input_weight)

    assert(result == test_bmi)

def test_bmi_over_weight():
    result = 0
    input_height = 1.65
    input_weight = 70
    test_bmi = 1 #"1" for overweight

    result = bmi.calculate_bmi(input_height,input_weight)

    assert(result == test_bmi)

def test_bmi_under_weight():
    result = 0
    input_height = 1.78
    input_weight = 40
    test_bmi = -1 #"-1" for underweight

    result = bmi.calculate_bmi(input_height,input_weight)

    assert(result == test_bmi)