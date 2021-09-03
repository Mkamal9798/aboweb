<head>
<link href="https://cdn.jsdelivr.net/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <ul>
        % for incident in list:
            <li><a target="_blank">{{incident}}</a></li>
        % end
    </ul>
    <script src="https://static.zdassets.com/zendesk_app_framework_sdk/2.0/zaf_sdk.min.js"></script>
    <script>
    var action = 'notifySuccess';
    </script>
    <script src="js/main.js"></script>
</body>


