import pytest
import white_elephant.state.gift as Gift
import white_elephant.state.player as Player
import white_elephant.state.rules as Rules
import white_elephant.state.game as Game
import white_elephant.actions.passAction as PassAction

@pytest.fixture
def names():
    return ["Paul","Leto","Chani","Jessica","Alia"]

@pytest.fixture
def giftList(names):
    giftList = list()
    i = 1
    for n in names:
        giftList.append(Gift.Gift(i, n + "'s Gift", n + ".com", "gs://" + n ))
        i+=1
    return giftList
         

@pytest.fixture
def playerList(names,giftList):
    playerList = list()
    for i in range(len(giftList)):
        playerList.append(Player.Player(i,names[i],giftList[i]))
    return playerList

@pytest.fixture
def exampleRules():
    exampleRules = Rules.Rules("default",3,True,False,False,0.0)
    return exampleRules

@pytest.fixture
def exampleGame(exampleRules,playerList):
    exampleGame = Game.Game(1,exampleRules,playerList)
    exampleGame.startGame()
    return exampleGame

# pass tests
def test_pass_do(exampleGame):
    originalPassCount = exampleGame.passCount
    originalunlockedPlayerCount = exampleGame.unlockedPlayerCount
    orignalIndex = exampleGame.index
    PassAction.PassAction.do(exampleGame)
    assert originalPassCount + 1 == exampleGame.passCount
    assert originalunlockedPlayerCount - 1 == exampleGame.unlockedPlayerCount
    assert exampleGame.players[exampleGame.index-1].isLocked is True
    assert orignalIndex + 1 == exampleGame.index
    
def test_pass_do_record(exampleGame):
    record = PassAction.PassAction.do(exampleGame)
    assert record.data['type'] == "pass"
    
def test_pass_undo(exampleGame):
    originalPassCount = exampleGame.passCount
    originalunlockedPlayerCount = exampleGame.unlockedPlayerCount
    orignalIndex = exampleGame.index
    record = PassAction.PassAction.do(exampleGame)
    PassAction.PassAction.undo(exampleGame,record)
    assert originalPassCount == exampleGame.passCount
    assert originalunlockedPlayerCount == exampleGame.unlockedPlayerCount
    assert exampleGame.players[exampleGame.index-1].isLocked is False
    assert orignalIndex == exampleGame.index