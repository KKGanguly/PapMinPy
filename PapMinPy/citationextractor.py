from bs4 import BeautifulSoup
from reference import Reference
from author import Author
from citationsnippet import CitationSnippet
import textwrap
import re
import os
import subprocess
import requests
from requests.exceptions import RequestException
import json
from jsonencoder import JSONEncoder
class CitationExtractor:
    soup=None
    def __init__(self,pdf):
        self.writeXml(self.convertPaperToXml(pdf),pdf)
        infile = open(pdf+".xml","r")
        contents = infile.read()
        self.soup = BeautifulSoup(contents,'xml')
    def convertPaperToXml(self,pdf):
        try:
            return subprocess.check_output([
                    "java",
                    "-cp","cermine-impl-1.13-jar-with-dependencies.jar",
                    "pl.edu.icm.cermine.PdfNLMContentExtractor",
                    "-path", pdf])
        except (RequestException,
                subprocess.CalledProcessError):
            return None
    def writeXml(self,output,pdf):
        with open(pdf+".xml", 'w') as xmlFile:
            xmlFile.write(output)
    def getCitationSnippets(self,references=None,json=False):
        candidateParagraphs=[]
        citationSnippets=[]
        paragraphs = self.soup.find_all('p')
        for para in paragraphs:
            if(para.find('xref')):
                candidateParagraphs.append(para)
        for candidateParagraph in candidateParagraphs:
            citations=candidateParagraph.find_all('xref')
            dedentedPara=textwrap.dedent(candidateParagraph.get_text().encode("utf-8")).strip()
            formattedPara=textwrap.fill(dedentedPara,width=80)
            formattedPara=re.sub(' +',' ',formattedPara)
            for citation in citations:
                edgeIds=citation.attrs['rid'].split()
                for edgeId in edgeIds:
                    citationSnippet = self.find(lambda citationSnippet: citationSnippet.edgeId == edgeId, citationSnippets)
                    if(citationSnippet is None):
                        citationSnippet=CitationSnippet()
                        citationSnippet.edgeId=edgeId
                    else:
                        citationSnippets.remove(citationSnippet)
                    if(formattedPara not in citationSnippet.paragraphs):
                        citationSnippet.paragraphs.append(formattedPara)
                    citationSnippets.append(citationSnippet)
        if json is True:
            citationSnippetJsons=[]
            for citationSnippet in citationSnippets:
                citationSnippetJsons.append(self.convertToJson(citationSnippet))
            return self.convertToJson(citationSnippets)
                
        return citationSnippets
    def find(self,f, seq):
        for item in seq:
            if f(item): 
              return item
    def convertToJson(self,obj):
        return json.dumps(obj, cls=JSONEncoder,indent=4, sort_keys=True)
    def convertToJsonDefault(self,obj):
        return json.dumps(obj)
    def getReferences(self,json=False):
        references=self.soup.find_all('ref')
        referenceList=[]
        for reference in references:
            extractedReference=Reference()
            try:
                extractedReference.id=reference.attrs['id']
            except AttributeError:
                print ('id not present')
                continue
            try:
                authors=reference.find_all('string-name')
                extractedReference.authors[:] = []
                for author in authors:
                    surname=author.find('surname').get_text().encode("utf-8")
                    givenName=author.find('given-names').get_text().encode("utf-8")
                    authorObject=Author()
                    authorObject.surname=surname
                    authorObject.givenName=givenName
                    extractedReference.authors.append(authorObject)
            except AttributeError:
                print ('author not present')
            try:
                extractedReference.year=reference.find('year').get_text().encode("utf-8")
            except AttributeError:
                print ('year not present')
            try:
                extractedReference.articleTitle=reference.find_all('article-title')[-1].get_text().encode("utf-8")
                print(extractedReference.articleTitle)
            except AttributeError:
                print ('article title not present')
            try:
                extractedReference.source=reference.find('source').get_text().encode("utf-8")
            except AttributeError:
                print ('source not present')
            try:
                extractedReference.volume=reference.find('volume').get_text().encode("utf-8")
            except AttributeError:
                print ('volume not present')
            try:
                extractedReference.fromPage=reference.find('fpage').get_text().encode("utf-8")
            except AttributeError:
                print ('fromPage not present')
            try:
                extractedReference.toPage=reference.find('lpage').get_text().encode("utf-8")
            except AttributeError:
                print ('toPage not present')
            referenceList.append(extractedReference)
        if json is True:
            referenceListJsons=[]
            for reference in referenceList:
                referenceListJsons.append(self.convertToJson(reference))
            return self.convertToJson(referenceList)
        return referenceList
