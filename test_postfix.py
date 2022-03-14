from postfix_eval import postfix_calc


def test_postfix_empty():
    ret = postfix_calc("")
    assert ret == None

def test_postfix_expression_valid():
    ret = postfix_calc("123++")
    assert ret == 6

def test_postfix_expression_string():
    ret = postfix_calc("abc++")
    assert ret == None