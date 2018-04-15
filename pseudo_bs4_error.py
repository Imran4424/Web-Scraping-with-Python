try:
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print()