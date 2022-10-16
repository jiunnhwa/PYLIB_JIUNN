

def slice_text(text, keyword="."): 
  """ returns a slice by keyword len - 1 element"""  
  return ((text, '' ) [text is None or keyword not in text].split(keyword)[0:-1] )


text = """
I think, therefore I am...
"""
print(slice_text(text))
print(slice_text(text,","))