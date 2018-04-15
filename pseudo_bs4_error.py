import scrapingtest

try:
    badContent = bsobj.nonExistingTag.anotherTag
except AttributeError as e:
    print("tag was not found")
else:
    if badContent == None:
        print("tag was n")
