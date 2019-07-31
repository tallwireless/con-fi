{% extends "main.tpl" %}


{% block content %}
    {% if error %}
        <p> There was an error in creating your account. Please try again shortly.</p>
    {% else %}
        {% if success %}
            <p>The account for {{ username }} has been created.</p>

            <p> Please head over to the <a href="/configure"> configuration </a> page
            for information on how to configure your device to connect to the wireless
            network. </p>
        {% else %}
            <p>There already exists an account for the {{ username }}. It is not
            possible to change your password. If you have forgotten your password,
            please created a new account.</p>
        {% endif %}
    {% endif %}
{% endblock %}
