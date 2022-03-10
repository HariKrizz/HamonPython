from average_nums import AverageofList

def test_average_of_list_ManyValue():
    ret = AverageofList([4,2,3])
    assert ret == 3 

def test_average_of_list_NoValue():
    ret = AverageofList([])
    assert ret == None
