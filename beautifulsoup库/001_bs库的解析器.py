from bs4 import BeautifulSoup

mk = '<html>data</html>'

BeautifulSoup(mk, 'html.parser') # bs4的HTML解析器

BeautifulSoup(mk, 'lxml') # lxml的HTML解析器

BeautifulSoup(mk, 'xml') # lxml的XML解析器

BeautifulSoup(mk, 'html5lib') # html5lib的解析器
