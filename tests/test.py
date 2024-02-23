from mypackage import myModule


def test_top_n():
    """
    make sur top_n works correctly
    """
    assert myModule.top_n([9,5,8,7,2,4],4) == [9,8,7,5], 'incorrect'
    assert myModule.top_n([10,12,8,9,2,5],2) == [12,10], 'incorrect'
    assert myModule.top_n([3,5,2,4,0],3) == [5,4,3], 'incorrect'