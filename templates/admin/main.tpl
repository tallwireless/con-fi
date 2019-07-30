<html>
    {% block head %}
    <head>
        <link href="/static/css/tent.css" rel="stylesheet">
        <title>BTV Wifi - {{ title }}</title>
    </head>
    {% endblock %}
    <body class="bg-color-primary">
        <div class="container padding-xs">
            <header class="masthead type-center bg-color-lightest">
               <a href="/"> <img style="width:200px" src="/static/btv-logo.png"></a>
                    <h3 class="subtitle subtitle-xl margin-xxs">{{ subtitle }}</h3>
            </header>
            <main class="mastcontent bg-color-lightest padding-xs">
            {% block content %}{% endblock %}
            </main>
        <footer class="mastfoot bg-color-secondary type-center">
            <span class="color-light"> Powered by <a target="_new"
                  href="https://github.com/tallwireless/con-fi">ConFi</a></span></footer>
        </div>
    </body>
</html>
