<head>
<link href="https://cdn.jsdelivr.net/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <ul>
        % for action in list:
            <li><a href="https://api.mahalo-app.io/aboweb/editeur/808/action?refEditeur=808&maxResults=10" target="_blank">{{action['clientName']}}</a></li>
        % end
    </ul>
    <script src="https://static.zdassets.com/zendesk_app_framework_sdk/2.0/zaf_sdk.min.js"></script>
    <script>
    var action = 'notifySuccess';
    </script>
    <script src="js/main.js"></script>
</body>


