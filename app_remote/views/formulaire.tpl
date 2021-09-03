<head>
  <link href="https://cdn.jsdelivr.net/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <form action="{{'incidentPost'}}" method="get">
    <label for="fname">refEditeur:</label><br>
    <input type="text" id="refEditeur" name="refEditeur" value="808"><br>
    <label for="lname">refAbonnements:</label><br>
    <input type="text" id="refAbonnements" name="refAbonnements" value="893137"><br>
    <label for="lname">dateDebut:</label><br>
    <input type="text" id='dateDebut' name='dateDebut' value="2021-07-24"><br><br>
    <input type="submit">
  </form> 


  <br> 
% if defined('error_msg'):
  <script src="https://static.zdassets.com/zendesk_app_framework_sdk/2.0/zaf_sdk.min.js"></script>
  <script>
    var action = 'notifyFailure';
    var msg = '{{error_msg}}';
  </script>
  <script src="js/main.js"></script>
% end



</body>