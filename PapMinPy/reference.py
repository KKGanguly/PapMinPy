from author import Author
class Reference:
    id=""
    authors=[]
    year=""
    articleTitle=""
    source=""
    volume=""
    fromPage=""
    toPage=""
    def __str__(self):
        string=''
        string+=self.getNoneSafeString(self.id)+" "
        if self.authors is not None:
            for author in self.authors:
                string+=self.getNoneSafeString(author.surname)+" "+self.getNoneSafeString(author.givenName)+" "
        string+=self.getNoneSafeString(self.year)+" "+self.getNoneSafeString(self.articleTitle)+" "+self.getNoneSafeString(self.source)+" "+self.getNoneSafeString(self.volume)+" "+self.getNoneSafeString(self.fromPage)+" "+self.getNoneSafeString(self.toPage)
        return string
    def getNoneSafeString(self,string):
        return '' if string is None else str(string)
