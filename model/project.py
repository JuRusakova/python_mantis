from sys import maxsize

class Project:
    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return "%s ; %s; %s" % (self.id, self.name, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.name is None or other.name is None or self.name == other.name)

    def sorting_name(self):
        if self.name:
            return self.name
        else:
            return maxsize
