{% extends "main.tpl" %}
{% block content %}
<p>Please use the following settings to connect to the BTV Wireless network.</p>

<p>
<b>SSID:</b> BTV<br />
<b>Security Type:</b> WPA2-Enterprise<br />
<b>EAP Method:</b> PEAP<br />
<b>Phase 2 (Inner Method):</b> MS-CHAPv2<br />
<b>Root CA:</b> <a href="/static/letsencrypt_ca.pem">Let's Encrypt CA</a> <br />
<b>Server Name:</b> wifi.blueteamvillage.org </b>
</p>
{% endblock %}
