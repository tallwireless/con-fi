{% extends "main.tpl" %}

{% block content %}
<p>Welcome to the Blue Team Village WiFi Registration Portal.
This form will created your credentials for being able to
login to the BTV SSID in the village this year.</p>

<p>These credentials should <b>NOT BE</b> any important passwords
    and should be a completely throw away password.  </p>
<p> Configuration instructions can be found <a
    href="/configure">here</a>.
</p>
<div class="container">
    <h4 class="subtitle subtitle-xl type-center margin-x margin-y">Create Creditals</h5>
        {% if  err_msg %}
        <div class="card card--filled card--tertiary card--filled
        card--outlined margin-xl margin-x">
        <div class="card__content">
        Please correct the following errors:
        <ul class="list">
            {% for msg in err_msg %}
            <li class="list__item">{{msg}}</li>
            {% endfor %}
        </ul>
        </div>
        </div>

        {% endif %}
    <div class="grid">
        <div class="grid__column "></div>
        <div class="grid__column">
    <form action="/create" method="post">
        <label class="control__label" for="username">Username:</label>
        <input type="text" width=25 name="username" id="username" class="control__input" value="{{ username }}">
        <label class="control__label" for="password">Password: <i>8 character
        min</i></label>
        <input type="password" width=25 class="control__input" id="password" name="password">
        <label class="control__label" for="verify_password">Veriy Password:</label>
        <input type="password" width=25 class="control__input" id="verify_password" name="verify_password">
        <label class="control__label"> Captcha: </label>
        <img src="/captcha.png?t={{ captcha }}" id="captcha">
        <input class="control_input" name="captcha" type="text">
        <input type="hidden" name="encrypt" value="{{ captcha }}">
        <div class="container type-center"><div class="display-inline">
        <input type="submit" class="control__button button button--filled button--primary" value="Create">
            </div></div>
    </form>
        </div>
        <div class="grid__column"></div>
</div>
{% endblock %}
