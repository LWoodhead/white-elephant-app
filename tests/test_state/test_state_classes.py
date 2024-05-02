import white_elephant.state.gift as Gift


def test_gift_constructor():
    testGift = Gift.Gift(1,"Garf","garf.com","gs://image/garf")
    assert testGift.id == 1

def test_gift_constructor_2():
    assert True is True 