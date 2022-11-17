"""
https://therenegadecoder.com/code/how-to-write-a-list-comprehension-in-python/

"""

"""
https://www.datasciencelearner.com/nested-list-comprehension-python/
flattened_list = [ ele for inner_list in outer_list for ele in inner_list]
df_data = [ parse_to_cols(line) for grp in groups for line in grp]
"""

txt = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1"/>
<title>Error 404 Not Found</title>
</head>
<body><h2>HTTP ERROR 404 Not Found</h2>
<table>

<tr><th>STATUS:</th><td>404</td></tr>
<tr><th>MESSAGE:</th><td>Not Found</td></tr>
<tr><th>SERVLET:</th><td>Stapler</td></tr>
</table>
</body>
</html>
"""

print( any([x for x in ['window.location.replace','Not found','Not Found'] if x in txt]))
 
