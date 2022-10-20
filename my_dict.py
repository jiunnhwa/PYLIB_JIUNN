
"""
Dictionary methods
https://onecompiler.com/python/3ykfgyunx
"""
dd = {'A': 1, None: 2, 'C': 3}
print (dd)


print("None elements:", {k: v for k, v in dd.items() if k is  None} )
print("non-None elements:", {k: v for k, v in dd.items() if k is not None})                    
print ("first and last element:", dict( [ (list(dd.items()))[i] for i in (0, -1)]))

lst = list(dd.items())
print('------ lst items -----', lst)
print('------ lst to dict -----', , dict([lst[0],lst[-1]] ))
