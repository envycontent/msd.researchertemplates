## Script (Python) "checkURLPrefix"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=urlstring
##title=
##
if urlstring.startswith('http://'):
    return urlstring
elif urlstring.startswith('https://'):
    return urlstring
else:
    return 'http://' + urlstring