import price_info

print("Test price_info")

def test_total_cost_shopping():
    result=0
    test = 46.75
    
    result = price_info.total_cost_shopping()
    
    assert(result==test)

def test_cost_of_fruits():
    result=0
    test = 12.6

    result = price_info.cost_of_fruits("orange",9)

    assert(result==test)