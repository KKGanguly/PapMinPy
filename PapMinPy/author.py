import json
class Author:
    surname=""
    givenName=""
    def toJSON(self):
        return dict(surname=self.surname,givenName=self.givenName)
