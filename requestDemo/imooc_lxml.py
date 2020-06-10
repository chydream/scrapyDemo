from lxml import etree


html_data = '''
<div>
  <ul>
       <li class="item-0"><a href="link1.html">first item</a></li>
       <li class="item-1"><a href="link2.html">second item</a></li>
       <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
       <li class="item-1"><a href="link4.html">fourth item</a></li>
       <li class="item-0"><a href="link5.html">fifth item</a>
   </ul>
</div>
'''

html = etree.HTML(html_data)
# print(etree.tostring(html).decode())
result = html.xpath("//li")
result = html.xpath("//li/@class")
result = html.xpath("//li/a[@href='link1.html']")
result = html.xpath("//li//span']")
print(result)