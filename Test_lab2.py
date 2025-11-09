import lab2 as lab

def test_find_min_max():
    assert lab.find_min_max([1,2,3,4,5]) == [1,5]
def test_calc_average():
    assert lab.calc_average([1,2,3,4,5]) == 3
def test_calc_median():
    assert lab.calc_median_temperature([1,2,3,9,5]) == 3