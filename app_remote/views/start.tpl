<head>
  <link href="https://cdn.jsdelivr.net/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

  <a class="btn btn-default btn-block"  href="incident?{{qs}}" role="button">Incidents</a>
% if defined('error_msg'):
  <script src="https://static.zdassets.com/zendesk_app_framework_sdk/2.0/zaf_sdk.min.js"></script>
  <script>
    var action = 'notifyFailure';
    var msg = '{{error_msg}}';
  </script>
  <script src="js/main.js"></script>
% end

  <a class="btn btn-default btn-block" href="action?{{qs}}" role="button">Actions</a>
% if defined('error_msg'):
  <script src="https://static.zdassets.com/zendesk_app_framework_sdk/2.0/zaf_sdk.min.js"></script>
  <script>
    var action = 'notifyFailure';
    var msg = '{{error_msg}}';
  </script>
  <script src="js/main.js"></script>
% end


  <a class="btn btn-default btn-block" href="suspension?{{qs}}" role="button">Suspensions</a>
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