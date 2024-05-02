class Gift:
    def __init__(self, id: int, title: str, link: str, image: str) -> None:
        self.id = id
        self.title = title
        self.link = link
        self.isOpen = True
        self.image = image
        self.stolenCount = 0
        
    def __str__(self) -> str:
        return "Gift(id: %d, title %s, link %s, isOpen: %r, stolenCount, %d" % (self.id,self.title,self.link,self.isOpen,self.stolenCount)
    
    def __eq__(self, value: object) -> bool:
        if(value is None):
            return False
        if(self.id is not value.id):
            return False
        if(self.title is not value.title):
            return False
        if(self.link is not value.link):
            return False
        if(self.isOpen is not value.isOpen):
            return False
        if(self.stolenCount is not value.stolenCount):
            return False
        return True
    
def test():
    assert True