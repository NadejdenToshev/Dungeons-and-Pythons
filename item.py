class Item:
    def __init__(self,item_type, description):
        self.item_type = item_type
        self.description = description

    def __repr__(self):
        return f"{self.item_type}: {self.description}"

