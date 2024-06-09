class Gift:
    def __init__(self, id: int, title: str, link: str, image: str) -> None:
        self.id = id
        self.title = title
        self.link = link
        self.isOpen = False
        self.image = image
        self.stolenCount = 0
        
    def __str__(self) -> str:
        return "Gift(id: %d, title %s, link %s, isOpen: %r, stolenCount, %d" % (
            self.id,self.title,self.link,self.isOpen,self.stolenCount)
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Gift):
            return False
        return (
            self.id == value.id and
            self.title == value.title and
            self.link == value.link and
            self.isOpen == value.isOpen and
            self.image == value.image and
            self.stolenCount == value.stolenCount
        )