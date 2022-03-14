from postfix_eval import postfix_calc


def test_postfix_empty():
    ret = postfix_calc("")
    assert ret == None
