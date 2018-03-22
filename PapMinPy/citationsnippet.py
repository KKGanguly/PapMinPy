class CitationSnippet:
    edgeId=""
    paragraphs=[]
    def __init__(self):
        self.paragraphs = []
    def toJSON(self):
        return dict(edgeId=self.edgeId,paragraphs=self.paragraphs)
