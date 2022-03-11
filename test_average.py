from average_nums import average

def test_average_ManyValue():
    ret = average([4,2,3])
    assert ret == 3 

def test_average_NoValue():
    ret = average([])
    assert ret == None

