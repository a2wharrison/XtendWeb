#!/usr/bin/python
import cgi
import cgitb
import os
import configparser
import codecs


__author__ = "Anoop P Alias"
__copyright__ = "Copyright Anoop P Alias"
__license__ = "GPL"
__email__ = "anoopalias01@gmail.com"


installation_path = "/opt/nDeploy"  # Absolute Installation Path
default_domain_data_file = installation_path+'/conf/domain_data_default.yaml'
app_template_file = installation_path+"/conf/apptemplates.yaml"
backend_config_file = installation_path+"/conf/backends.yaml"


cgitb.enable()

form = cgi.FieldStorage()

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
print('<a href="xtendweb.cgi" data-toggle="tooltip" data-placement="bottom" title="Start Over"><span class="glyphicon glyphicon-globe" aria-hidden="true"></span></a>')
print('<h4>XtendWeb</h4>')
print('</div>')
print('<ol class="breadcrumb">')
print('<li><a href="xtendweb.cgi"><span class="glyphicon glyphicon-repeat"></span></a></li>')
print('<li class="active">Server Config</li>')
print('</ol>')

if form.getvalue('poolfile') and form.getvalue('thekey') and form.getvalue('section'):
    myphpini = form.getvalue('poolfile')
    mysection = int(form.getvalue('section'))
    if os.path.isfile(myphpini):
        config = configparser.ConfigParser()
        config.readfp(codecs.open(myphpini, 'r', 'utf8'))
        # Next section start here
        print('<div class="panel panel-default">')  # marker6
        print('<div class="panel-heading"><h3 class="panel-title">Edit PHP-FPM pool: '+config.sections()[mysection]+'</h3></div>')
        print('<div class="panel-body">')  # marker7
        myconfig = dict(config.items(config.sections()[mysection]))
        print('<form class="form-group" action="save_phpfpm_pool_file.cgi">')
        print('<ul class="list-group">')
        print('<li class="list-group-item">')
        print('<div class="row">')
        print('<div class="col-sm-6 col-radio">')
        print(form.getvalue('thekey'))
        print('</div>')
        print('<div class="col-sm-6 col-radio">')
        print('<input class="form-control" placeholder='+myconfig.get(form.getvalue('thekey', ''))+' type="text" name="thevalue">')
        print('</div>')
        print('</div>')
        print('</li>')
        print(('<input style="display:none" name="poolfile" value="'+form.getvalue('poolfile')+'">'))
        print(('<input style="display:none" name="thekey" value="'+form.getvalue('thekey')+'">'))
        print(('<input style="display:none" name="section" value="'+form.getvalue('section')+'">'))
        print('<br>')
        print('<input class="btn btn-primary" type="submit" value="Submit">')
        print('</ul>')
        print('</form>')
        print('</div>')  # div8
        print('</div>')  # div7
else:
        print('<div class="alert alert-info"><span class="glyphicon glyphicon-alert" aria-hidden="true"></span> Forbidden </div>')
print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
print('</div>')  # marker3
print('</div>')  # marker2
print('</body>')
print('</html>')
