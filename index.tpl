<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="style.css">


    <style>
        h2 {color:blue;}
        p {color:black;}

table.minimalistBlack {
  border: 2px solid #000000;
  width: 100%;
  text-align: left;
  border-collapse: collapse;
}
table.minimalistBlack td, table.minimalistBlack th {
  border: 1px solid #000000;
  padding: 4px 3px;
}
table.minimalistBlack tbody td {
  font-size: 13px;
}
table.minimalistBlack thead {
  background: #CFCFCF;
  background: -moz-linear-gradient(top, #dbdbdb 0%, #d3d3d3 66%, #CFCFCF 100%);
  background: -webkit-linear-gradient(top, #dbdbdb 0%, #d3d3d3 66%, #CFCFCF 100%);
  background: linear-gradient(to bottom, #dbdbdb 0%, #d3d3d3 66%, #CFCFCF 100%);
  border-bottom: 3px solid #000000;
}
table.minimalistBlack thead th {
  font-size: 15px;
  font-weight: bold;
  color: #000000;
  text-align: left;
}
table.minimalistBlack tfoot {
  font-size: 14px;
  font-weight: bold;
  color: #000000;
  border-top: 3px solid #000000;
}
table.minimalistBlack tfoot td {
  font-size: 14px;
}        
    </style>

    </head>

    <body>
        <div id='div_01'>
        {{ report_1 }}
        </div>    

        <div id='div_02' style='background-color: azure' >
        {{ report_2 }}
        </div>    

        <div id='div_03' style='background-color: khaki' >
        {{ report_3 }}
        </div>         

        <p {{style_p}}>hello </p>

        <button onclick="myFunction()">Toggle</button>
        <div id='div_04'>
        {{ report_4 }}
        </div>    


    <script src="index.js"></script>
    </body>
     <script>
     function myFunction() {
        var x = document.getElementById("report04");
        x.style.display = x.style.display === "none"?"block":"none";
        }     
     </script>
    



</html>