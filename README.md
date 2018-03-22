# PapMinPy
> A Python Library to extract information from academic papers. 

Paper Miner (PapMinPy) is a library to extract information from academic paper PDFs. Currently, the paper can be converted into structured XML, references can be extracted with separate reference information (i.e., author, title etc.) and citations inside papers can be extracted.

## Installation

```sh
pip install git+https://github.com/KKGanguly/PapMinPy
```
This project uses [CERMINE](https://github.com/CeON/CERMINE) java library for its purpose, so [JDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) must be installed.
## Usage example

First, create the CitationExtractor object with the following code.
```python
from PapMinPy import citationextractor
citationExtractor=citationextractor.CitationExtractor("pdfFileName.pdf")
```
Now, the references can be extracted using the following code.
```python
citationExtractor.getReferences(True)
```
To get the output as objects, rather than JSONs, simply use -
```python
citationExtractor.getReferences(False)
```
The citation snippets (paragraphs containing a specific citation) can be found utilizing - 
```python
citationExtractor.getCitationSnippets(json=True)
```
## Release History

* 0.1a
    * CHANGE: Added inital release (alpha)
* 0.1b
    * Work in progress  

## Meta

Kishan Kumar Ganguly – kkganguly.iit.du@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/KKGanguly](https://github.com/KKGanguly/)

## Contributing

1. Fork it (<https://github.com/KKGanguly/PapMinPy/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki