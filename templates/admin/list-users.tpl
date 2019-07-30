{% extends "admin/main.tpl" %}

{% block content %}
<p> Below are the currently confiured account:</p>

<table class="table table--strpped">
    <thead class="table__head">
        <tr class="table__row table__row--headding">
            <th class="table__cell">username</th>
            <th class="table__cell">password</th>
            <th class="table__cell">role</th>
        </tr>
    </thead>
    <tbody class="table__body">
        {% for user in users %}
        <tr class="table__head">
            <td class="table__cell">{{user.username}}</th>
            <td class="table__cell">{{user.password}}</th>
            <td class="table__cell">{{user.role}}</th>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
