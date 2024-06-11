import white_elephant.state.gift as Gift
import white_elephant.state.player as Player
import white_elephant.state.rules as Rules
import white_elephant.state.game as Game
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

@pytest.fixture
def exampleRules():
    exampleRules = Rules.Rules("Example",3,True,False,False,0.0)
    return exampleRules

@pytest.fixture
def cloneExampleRules(exampleRules):
    cloneExampleRules = copy.deepcopy(exampleRules)
    return cloneExampleRules

@pytest.fixture
def playerList(gary):
    playerList = [gary]
    return playerList

@pytest.fixture
def exampleGame(exampleRules,playerList):
    exampleGame = Game.Game(1,exampleRules,playerList)
    return exampleGame

@pytest.fixture
def cloneExampleGame(exampleGame):
    cloneExampleGame = copy.deepcopy(exampleGame)
    return cloneExampleGame

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
    assert gary.isLocked is False

def test_player_compare(gary,cloneGary):
    assert gary == cloneGary
    assert gary is not None

#Rules tests
def test_rules_constructor(exampleRules):
    assert exampleRules.name == "Example"
    assert exampleRules.maxStealCount == 3
    assert exampleRules.randomizeRoundOrder is True
    assert exampleRules.bonusGift is False
    assert exampleRules.bonusSteal is False
    assert exampleRules.stealFailChance == 0.0
    
def test_rules_compare(exampleRules, cloneExampleRules):
    assert exampleRules == cloneExampleRules
    assert exampleRules is not None
    
#Game tests
def test_game_constructor(exampleGame, exampleRules, playerList):
    assert exampleGame.id == 1
    assert exampleGame.rules == exampleRules
    assert exampleGame.players == playerList
    assert exampleGame.index is None
    assert exampleGame.passCount is None
    assert exampleGame.unlockedPlayerCount is None 
    assert exampleGame.playerCount is None
    assert exampleGame.closedGiftCount is None
    assert exampleGame.isStarted is False
    
def test_game_compare(exampleGame,cloneExampleGame):
    assert exampleGame == cloneExampleGame
    assert exampleGame is not None
    
def test_start_game(exampleGame,cloneExampleGame,playerList):
    assert exampleGame.index is None
    assert exampleGame.passCount is None
    assert exampleGame.unlockedPlayerCount is None 
    assert exampleGame.playerCount is None
    assert exampleGame.closedGiftCount is None
    assert exampleGame.isStarted is False
    exampleGame.startGame()
    assert exampleGame.index == 0
    assert exampleGame.passCount == 0
    assert exampleGame.unlockedPlayerCount == len(playerList) 
    assert exampleGame.playerCount == len(playerList)
    assert exampleGame.closedGiftCount == len(playerList)
    assert exampleGame.isStarted is True