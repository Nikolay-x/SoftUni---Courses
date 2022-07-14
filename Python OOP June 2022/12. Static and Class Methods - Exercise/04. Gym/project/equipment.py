class Equipment:
    ID = 1

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        id = Equipment.ID
        Equipment.ID += 1
        return id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
