#!/usr/bin/python3
import mg_python
import sys
import os
import cgi, cgitb
cnt=0
form=cgi.FieldStorage()
glbal=form.getvalue('global')
if (glbal[0:1] != "^"):
    glbal="^" + glbal
mg_python.m_set_host(0, "yottadb", 7041, "", "")
jsonstr='[{ "name": "' + glbal + '", "class": "man", "textClass": "emphasis"'
key = mg_python.m_order(0, glbal, "")
if (key==""):
   print("Content-type: text/html\n\n")
   print("\r\n<html>\r\n")
   print("<body>\r\n")
   print("<p><h1>There is no data in the global " + glbal + "</h1></p>\r\n")
   print("</body>\r\n")
   print("</html>\r\n")
   sys.exit(0)
while (key != ""):
   cnt=cnt+1
   if (cnt==1):
      jsonstr=jsonstr + ', "children": [ { "name": "' + key + '", "class": "man" '
      if (mg_python.m_get(0, glbal, key) != ""):
             jsonstr=jsonstr + ',"extra": { "nickname": "' + mg_python.m_get(0, glbal, key) + '" }'
   else:
      jsonstr=jsonstr + ', { "name": "' + key +'", "class": "man"'
      if (mg_python.m_get(0, glbal, key) != ""):
             jsonstr=jsonstr + ',"extra": { "nickname": "' + mg_python.m_get(0, glbal, key) + '" }'
   key1 = mg_python.m_order(0, glbal, key, "")
   if (key1==""):
      jsonstr=jsonstr + "}"
   cnt1=0
   while (key1 != ""):
      cnt1=cnt1+1
      if (cnt1==1):
         jsonstr=jsonstr + ', "children": [ { "name": "' + key1 + '", "class": "man"'
         if (mg_python.m_get(0, glbal, key, key1) != ""):
             jsonstr=jsonstr + ',"extra": { "nickname": "' + mg_python.m_get(0, glbal, key, key1) + '" }'
      else:
         jsonstr=jsonstr + ', { "name": "' + key1 + '", "class": "man"'
         if (mg_python.m_get(0, glbal, key, key1) != ""):
             jsonstr=jsonstr + ',"extra": { "nickname": "' + mg_python.m_get(0, glbal, key, key1) + '" }'
      key2 = mg_python.m_order(0, glbal, key, key1, "")
      if (key2 == ""):
         jsonstr=jsonstr + "}"
      cnt2=0
      while (key2 != ""):
         cnt2=cnt2+1
         if (cnt2==1):
            jsonstr=jsonstr + ', "children": [ { "name": "' + key2 + '", "class": "man"'
            if (mg_python.m_get(0, glbal, key, key1, key2) != ""):
               jsonstr=jsonstr + ',"extra": { "nickname": "' + mg_python.m_get(0, glbal, key, key1, key2) + '" }'
         else:
            jsonstr=jsonstr + ', { "name": "' + key2 + '", "class": "man"'
         key3 = mg_python.m_order(0, glbal, key, key1, key2,"")
         if (mg_python.m_get(0, glbal, key, key1, key2) != ""):
            jsonstr=jsonstr + ',"extra": { "nickname": "' + mg_python.m_get(0, glbal, key, key1, key2) + '" }'
         if (key3 == ""):
            jsonstr=jsonstr + "}"
         cnt3=0
         while (key3 != ""):
            cnt3=cnt3+1
            if (cnt3==1):
               jsonstr=jsonstr + ', "children": [ { "name": "' + key3 + '", "class": "man"'
               if (mg_python.m_get(0, glbal, key, key1, key2, key3) != ""):
                  jsonstr=jsonstr + ',"extra": { "nickname": "' + mg_python.m_get(0, glbal, key, key1, key2, key3) + '" }'
            else:
               jsonstr=jsonstr + ', { "name": "' + key3 + '", "class": "man"'
            key4 = mg_python.m_order(0, glbal, key, key1, key2, key3,"")
            if (mg_python.m_get(0, glbal, key, key1, key2, key3) != ""):
               jsonstr=jsonstr + ',"extra": { "nickname": "' + mg_python.m_get(0, glbal, key, key1, key2, key3) + '" }'
            if (key4 == ""):
                jsonstr=jsonstr + "}"
            cnt4=0
            while (key4 != ""):
               cnt4=cnt4+1
               if (cnt4==1):
                  jsonstr=jsonstr + ', "children": [ { "name": "' + key4 + '", "class": "man"'
                  if (mg_python.m_get(0, glbal, key, key1, key2, key3, key4) != ""):
                     jsonstr=jsonstr + ',"extra": { "nickname": "' + mg_python.m_get(0, glbal, key, key1, key2, key3, key4) + '" }'
               else:
                  jsonstr=jsonstr + ', { "name": "' + key4 + '", "class": "man"'
                  if (mg_python.m_get(0, glbal, key, key1, key2, key3, key4) != ""):
                     jsonstr=jsonstr + ',"extra": { "nickname": "' + mg_python.m_get(0, glbal, key, key1, key2, key3, key4) + '" }'
               key5 = mg_python.m_order(0, glbal, key, key1, key2, key3, key4, "")
               if (key5==""):
                  jsonstr=jsonstr + '}'
               key4 = mg_python.m_order(0, glbal, key, key1, key2, key3, key4)
               if (key4==""):
                  jsonstr=jsonstr + ']}'
            key3 = mg_python.m_order(0, glbal, key, key1, key2, key3)
            if (key3==""):
               jsonstr=jsonstr + ']}'
         key2 = mg_python.m_order(0, glbal, key, key1, key2)
         if (key2==""):
            jsonstr=jsonstr + ']}'
      key1  = mg_python.m_order(0, glbal, key, key1)
      if (key1==""):
            jsonstr=jsonstr + ']}'
   key  = mg_python.m_order(0, glbal, key)
   if (key==""):
      jsonstr=jsonstr + ']}]'
print("Content-type: text/html\n\n")
print('<!DOCTYPE html>\r\n')
print('<html lang="en">\r\n')
print('<meta charset="utf-8">\r\n')
print('<link rel="stylesheet" href="demo.css">\r\n')
print("<script>const jsonstr='" + jsonstr + "';console.log(jsonstr);</script>")
print('<script src="https://cdn.jsdelivr.net/lodash/4.17.4/lodash.min.js"></script>\r\n')
print('<script src="https://d3js.org/d3.v4.min.js"></script>\r\n')
print('<script src="dTree.min.js"></script>\r\n')
print('<script src="demo1.js"></script>\r\n')
print('<body>\r\n')
print('		<h1>Global Viewer</h1>\r\n')
print('<div><p>Shift + Double Left Click to Zoom Out</p><p>Double Left Click to Zoom In</p></div></br></br>\r\n')
print('    <div id="graph"></div>\r\n')
print('</body>\r\n')
print('</html>\r\n')
