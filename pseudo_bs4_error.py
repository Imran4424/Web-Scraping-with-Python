import scrapingtest

try:
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print("tag was not found")