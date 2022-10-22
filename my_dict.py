
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
print('------ lst to dict -----', dict([lst[0],lst[-1]] ))


"""
https://onecompiler.com/python/3ykcqykvb
"""
def hhmmss_to_seconds(hhmmss):
    vals = hhmmss.split(':')
    h = int(vals[0])
    m = int(vals[1])
    s = int(vals[2])
    return (h*3600)+(m*60)+s    
    
def duration_sort(durations):
    """ Returns the list of jobs ordered descendingly from durations converted to seconds  """
    return sorted(list(enumerate(list(map(hhmmss_to_seconds, durations)))), key=lambda x: x[1], reverse=True)
    
   
durations = ['00:15:00','00:06:00']    
print(hhmmss_to_seconds('0:15:10'))
print(duration_sort(durations))


"""
https://onecompiler.com/python/3ykjsc5py
"""
def duration_sort(arguments, durations):
    """ returns the list of jobs ordered descendingly from durations converted to seconds  """
    sorted_duras = sorted(list(enumerate(list(map(hhmmss_to_seconds, durations)))), key=lambda x: x[1], reverse=True)
    return [arguments[item[0]] for item in sorted_duras], [durations[item[0]] for item in sorted_duras]

arguments = ['A', 'B', 'C']
durations = ['00:00:10', '00:11:00', '12:00:00']

print(duration_sort(arguments, durations))


"""
https://onecompiler.com/python/3ykjsyez7
"""

def dict_sort_by_param(dict_obj, sort_value, reverse=True):
    """return a reverse(default) sorted dict by parameter"""
    return {key: dict_obj[key] for key in sorted(dict_obj, key=lambda x: (dict_obj[x][sort_value]), reverse=reverse)}
    # return dict(sorted(dict_obj.items(), key=lambda x: x[1][sort_value], reverse=reverse))
    # sorted_builds = {key: builds[key] for key in sorted(builds, key=lambda x:(builds[x][sort_value]))}
    # sorted_builds = {key: builds[key] for key in sorted(builds, key=lambda x:(builds[x].get(sort_value,0)))}
    
    
test_dict = {
              'Alpha' :  {'name' : 'Alpha',  'run_duration' : 10},
              'Bravo' :  {'name' : 'Bravo',  'run_duration' : 200},
              'Charlie' :{'name' : 'Charlie','run_duration' : 30},
            }
             
print(test_dict)  
print(dict_sort_by_param(test_dict, 'run_duration'))  
print(dict_sort_by_param(test_dict, 'name'))  

# sort list of tuples from dictionary
lst = [(key, test_dict[key]['run_duration']) for key in test_dict.keys()]  
lst.sort(key=lambda x: x[1], reverse=True)  
print(lst)  




# make unique set
lst = ['A', 'A', 10, 5, 5]
print(list(dict.fromkeys(lst)))
print(list(set(lst))) #order may not be preserved

 