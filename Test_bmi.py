import Lab2.bmi as bmi
print("Test lab2 bmi")

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.77,59) == 0
def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.77,90) == 1
def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.77,50) == -1
