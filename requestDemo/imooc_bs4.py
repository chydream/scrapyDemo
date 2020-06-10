import re

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --><span>Elsie</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

print(soup.select(".panel .panel-heading"))
for ul in soup.select(".panel .panel-heading"):
    print(ul['id'])

# print(soup.find_all(name='a'))
# print(soup.find_all(attrs={"id": "list-1"}))
# print(soup.find_all(id="list-1"))
# print(soup.find_all(class_="list"))
# print(soup.find_all(text=re.compile("Foo")))
# print(soup.find(name="a"))  # 返回的是一个单个的元素
# print(soup.p.contents)
# print(soup.p.children)
# for i in soup.p.children:
#     print(i )
#
# print(soup.p.descendants)
# for i in soup.p.descendants:
#     print(i)
#
# print(soup.s.parent)
# print(soup.s.parents)
# print(soup.a.next_sibling)
# print(soup.a.previous_sibling)
# print(soup.a.next_siblings)
# print(soup.a.previous_siblings)


# print(soup.prettify())
# print(soup.title.string)
# print(soup.head.string)
# print(soup.p)
# print(soup.title.name)
# print(soup.p.attrs)
# print(soup.p['class'])
# print(soup.head.title)