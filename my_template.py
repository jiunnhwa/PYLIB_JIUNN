from my_file import file_writetext, file_readalltext
from jinja2 import Environment
import pandas as pd

# double = lambda x: x * 2
to_td = lambda elem: f'<td>{elem}</td>'
to_tr = lambda row: f"<tr>{ ''.join([ to_td(val) for val in  row])  }</tr>"
to_th = lambda hdr: f"<thead><tr>{ ''.join([ f'<th>{val}</th>' for val in hdr])  }</tr></thead>"
to_table = lambda str: f'<table>{str}</table>'
to_div = lambda str: f'<div>{str}</div>'
to_li = lambda elem: f'<li>{elem}</li>'
to_href = lambda link,text: f'<a href="{link}">{text}</a>'


print( *[to_td(x) for x in ['r1c1', 'r1c2'] ] )

def set_attribute(html_tag_fragment, attr):
  """add attributes to a tag """
  pre, suf = html_tag_fragment.split(' ')
  return pre + attr + suf

def style_adder(html_fragment, styles ):
    # handle double quotes
    pre = html_fragment if "style=" in html_fragment else "style="
    return (pre + "'" + " ".join(styles) + "'").replace("''"," ").replace('="',"='").replace('"\''," ")

def to_report(report_dict):
  """report consists of paras and datatable"""
  title, hdr, data = report_dict['title'], report_dict['header'], report_dict['data']
  para = f"<p {report_dict.get('style') }> {report_dict.get('para')} </p>" if 'para' in report_dict else ""
  tbl = (to_table(to_th(hdr)  + "\n".join( [to_tr(row) for row in data] ))) 
  tbl = tbl.replace('<table>', f"<table class='minimalistBlack' id='{report_dict['id']}'>")
  return f'<h2>{title}</h2>'+ tbl + para 


df_to_tuples = lambda df: list(df.itertuples(index=False, name=None ))
df_colnames_to_tuples = lambda df: tuple(list(df_275))
def get_df():
  data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
  }
  return df_to_tuples(pd.DataFrame(data))


report1 = {
  'id': 'report01',
  'title': "Report 1",
  'header' :('Company','Contact','Country'),
  'data' : [('Alfreds','Maria','Germany'), ('Ernst','Roland','Austria')]
}

report2 = {
  'id': 'report02',
  'title': "Report 2",
  'header' :('calories','duration'), 
  'data' : get_df(),
  'para' : "this is the result 2....",
  'style': style_adder("style='color: blue;'", ['background-color: orange;','font-weight: bold;', 'text-align: left;'])
}

report3 = {
  #  required
  'id': 'report03',
  'title': "Report 3",
  'header' :('A','B'), 
  'data' :  df_to_tuples(pd.DataFrame({"A":[3,4],"B":[5,6]}, index=["a","b"])),
  # additional
  'para' : "this is the result",
  'style': style_adder('style="color: red;"', ['background-color: orange;','font-weight: bold;', 'text-align: left;'])
}

df_275 = pd.read_csv('275.csv',header= 0)
df_275 = df_275.drop(['Inc', 'Rank' , 'Stab Status', 'Stab Duration', 'Stab NA', 'Stab NE', 'Stab NC', 'Stab KO', 'Stab OK', 'Stab NAN', 'VBProj', 'Partition', 'Reason', 'Result Report', 'Check Report', 'Log Report' ], axis=1) 
df_275.insert(0, 'Build', '275')
# print( tuple(list(df_275)))

report4 = {
  'id': 'report04',
  'title': "Build 275",
  'header' : df_colnames_to_tuples(df_275), #tuple(list(df_275)), 
  'data' :df_to_tuples(df_275)
}


_html = ( Environment().from_string(file_readalltext("index.tpl")).render( 
    { 
      'title':'Test Diff Report', 
      'report_1': to_report(report1),
      'report_2': to_report(report2),
      'report_3': to_report(report3),
      'report_4': to_report(report4),
      'style_p': style_adder("", ['background-color: yellow;','font-weight: bold;', 'text-align: left;'])

        
    } 
  )
  )

file_writetext("index.html", _html)



# *************************************************************

