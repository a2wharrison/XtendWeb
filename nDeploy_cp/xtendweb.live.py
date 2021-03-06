#!/usr/bin/env python


import os
import socket
import yaml
import cgitb
try:
    import simplejson as json
except ImportError:
    import json


__author__ = "Anoop P Alias"
__copyright__ = "Copyright Anoop P Alias"
__license__ = "GPL"
__email__ = "anoopalias01@gmail.com"


installation_path = "/opt/nDeploy"  # Absolute Installation Path
cluster_config_file = installation_path+"/conf/ndeploy_cluster.yaml"


cgitb.enable()


def close_cpanel_liveapisock():
    """We close the cpanel LiveAPI socket here as we dont need those"""
    cp_socket = os.environ["CPANEL_CONNECT_SOCKET"]
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(cp_socket)
    sock.sendall('<cpanelxml shutdown="1" />')
    sock.close()


close_cpanel_liveapisock()
cpaneluser = os.environ["USER"]
cpuserdatajson = "/var/cpanel/userdata/" + cpaneluser + "/main.cache"
with open(cpuserdatajson, 'r') as cpaneluser_data_stream:
    json_parsed_cpaneluser = json.load(cpaneluser_data_stream)
main_domain = json_parsed_cpaneluser.get('main_domain')
# parked_domains = yaml_parsed_cpaneluser.get('parked_domains')   # This data is irrelevant as parked domain list is in ServerAlias
addon_domains_dict = json_parsed_cpaneluser.get('addon_domains')     # So we know which addon is mapped to which sub-domain
sub_domains = json_parsed_cpaneluser.get('sub_domains')

# Settings Lock
if os.path.exists("/var/cpanel/users.cache/" + cpaneluser):
    with open("/var/cpanel/users.cache/" + cpaneluser) as users_file:
        json_parsed_cpusersfile = json.load(users_file)
    hostingplan_filename = json_parsed_cpusersfile.get('PLAN', 'default').encode('utf-8').replace(' ', '_')
else:
    hostingplan_filename = 'default'
if hostingplan_filename == 'undefined' or hostingplan_filename == 'default':
    if os.path.isfile(installation_path+"/conf/domain_data_default_local.yaml"):
        TEMPLATE_FILE = installation_path+"/conf/domain_data_default_local.yaml"
    else:
        TEMPLATE_FILE = installation_path+"/conf/domain_data_default.yaml"
else:
    if os.path.isfile(installation_path+"/conf/domain_data_default_local_"+hostingplan_filename+".yaml"):
        TEMPLATE_FILE = installation_path+"/conf/domain_data_default_local_"+hostingplan_filename+".yaml"
    else:
        if os.path.isfile(installation_path+"/conf/domain_data_default_local.yaml"):
            TEMPLATE_FILE = installation_path+"/conf/domain_data_default_local.yaml"
        else:
            TEMPLATE_FILE = installation_path+"/conf/domain_data_default.yaml"
with open(TEMPLATE_FILE, 'r') as templatefile_data_stream:
    yaml_parsed_templatefile = yaml.safe_load(templatefile_data_stream)
settings_lock = yaml_parsed_templatefile.get('settings_lock', 'disabled')

print('Content-Type: text/html')
print('')
print('<html>')
print('<head>')
print('<title>XtendWeb</title>')
print(('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">'))
print(('<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" crossorigin="anonymous"></script>'))
print(('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>'))
print(('<script src="js.js"></script>'))
print(('<link rel="stylesheet" href="styles.css">'))
print('</head>')
print('<body>')
print('<div id="main-container" class="container text-center">')  # marker1
print('<div class="row">')  # marker2
print('<div class="col-md-6 col-md-offset-3">')  # marker3
print('<div class="logo">')
print('<a href="xtendweb.live.py" data-toggle="tooltip" data-placement="bottom" title="Start Over"><span class="glyphicon glyphicon-globe" aria-hidden="true"></span></a>')
print('<h4>XtendWeb</h4>')
print('</div>')
print('<ol class="breadcrumb">')
print('<li><a href="xtendweb.live.py"><span class="glyphicon glyphicon-repeat"></span></a></li>')
print('<li class="active">Select domain</li>')
print('</ol>')
# Next section start here
print('<div class="panel panel-default single">')  # marker6
print('<div class="panel-heading"><h3 class="panel-title">Switch domains automatically</h3></div>')
print('<div class="panel-body">')  # marker7
if settings_lock == 'enabled':
    print(('<div class="alert alert-info alert-top">Application Server settings are locked by the administrator</div>'))
else:
    print('<form class="form-group" action="autoswitch.live.py">')
    print('<input class="btn btn-primary" type="submit" value="AUTO SWITCH TO NGINX">')
    print(('<input class="hidden" name="cpaneluser" value="'+cpaneluser+'">'))
    print('</form>')
print('</div>')  # marker7
print('</div>')  # marker6
# Next section start here
print('<div class="panel panel-default">')  # marker4
print('<div class="panel-heading"><h3 class="panel-title">Select domain to configure manually</h3></div>')
print('<div class="panel-body">')  # marker5
print('<form class="form-inline" action="app_settings.live.py" method="post">')
print('<select name="domain">')
print(('<option value="'+main_domain+'">'+main_domain+'</option>'))
for domain_in_subdomains in sub_domains:
    if domain_in_subdomains not in addon_domains_dict.values():
        if domain_in_subdomains.startswith("*"):
            wildcard_domain = "_wildcard_."+domain_in_subdomains.replace('*.', '')
            print(('<option value="'+wildcard_domain+'">'+domain_in_subdomains+'</option>'))
        else:
            print(('<option value="'+domain_in_subdomains+'">'+domain_in_subdomains+'</option>'))
for the_addon_domain in addon_domains_dict.keys():
    print(('<option value="'+addon_domains_dict.get(the_addon_domain)+'">'+the_addon_domain+'</option>'))
print('</select>')
print('<input class="btn btn-primary" type="submit" value="CONFIGURE">')
print('</form>')
print('</div>')  # marker5
print('</div>')  # marker4
print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
print('</div>')  # marker3
print('</div>')  # marker2
print('</div>')  # # marker1
print('</body>')
print('</html>')
