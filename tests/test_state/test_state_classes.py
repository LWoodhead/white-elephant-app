import white_elephant.state.gift as Gift
import white_elephant.state.player as Player
import pytest
import copy

@pytest.fixture
def garyGift():
    garyGift = Gift.Gift(1,"Garf","garf.com","gs://image/garf")
    return garyGift

@pytest.fixture
def cloneGaryGift(garyGift):
    cloneGaryGift = copy.deepcopy(garyGift)
    return cloneGaryGift

@pytest.fixture
def gary(garyGift):
    gary = Player.Player(1,"Gary",garyGift)
    return gary

@pytest.fixture
def cloneGary(gary):
    cloneGary = copy.deepcopy(gary)
    return cloneGary

#Gift tests   
def test_gift_constructor(garyGift):
    assert garyGift.id == 1
    assert garyGift.title == "Garf"
    assert garyGift.link == "garf.com"
    assert garyGift.isOpen is not True
    assert garyGift.image == "gs://image/garf"
    assert garyGift.stolenCount == 0
    
def test_gift_compare(garyGift,cloneGaryGift):
    assert garyGift == cloneGaryGift
    assert garyGift is not None

#Player tests
def test_player_constructor(gary, garyGift):
    assert gary.id == 1
    assert gary.name == "Gary"
    assert gary.originalGift == garyGift
    assert gary.gameGift is None
    assert gary.isLocked is not True

def test_player_compare(gary,cloneGary):
    assert gary == cloneGary
    assert gary is not None
    
def test_fail():
    assert False