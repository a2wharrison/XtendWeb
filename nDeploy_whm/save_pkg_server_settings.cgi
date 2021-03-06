#!/usr/bin/python
import cgi
import cgitb
import os
import yaml
import sys
import re


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

if form.getvalue('cpanelpkg'):
    if form.getvalue('cpanelpkg') == 'default':
        pkgdomaindata = installation_path+'/conf/domain_data_default_local.yaml'
    else:
        pkgdomaindata = installation_path+'/conf/domain_data_default_local_'+form.getvalue('cpanelpkg')+'.yaml'
    if os.path.isfile(pkgdomaindata):
        # Get all config settings from the domains domain-data config file
        with open(pkgdomaindata, 'r') as profileyaml_data_stream:
            yaml_parsed_profileyaml = yaml.safe_load(profileyaml_data_stream)
    current_redirecturl = yaml_parsed_profileyaml.get('redirecturl', "none")
    # set_expire_static
    if 'set_expire_static' in form.keys():
        set_expire_static = form.getvalue('set_expire_static')
        yaml_parsed_profileyaml['set_expire_static'] = set_expire_static
    else:
        print('ERROR: Forbidden::set_expire_static')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # settings_lock
    if 'settings_lock' in form.keys():
        settings_lock = form.getvalue('settings_lock')
        yaml_parsed_profileyaml['settings_lock'] = settings_lock
    else:
        print('ERROR: Forbidden::settings_lock')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # phpmaxchildren
    if 'phpmaxchildren' in form.keys():
        phpmaxchildren = form.getvalue('phpmaxchildren')
        yaml_parsed_profileyaml['phpmaxchildren'] = phpmaxchildren
    else:
        print('ERROR: Forbidden::phpmaxchildren')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # mod_security
    if 'mod_security' in form.keys():
        mod_security = form.getvalue('mod_security')
        yaml_parsed_profileyaml['mod_security'] = mod_security
    else:
        print('ERROR: Forbidden::mod_security')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # autoindex
    if 'autoindex' in form.keys():
        autoindex = form.getvalue('autoindex')
        yaml_parsed_profileyaml['autoindex'] = autoindex
    else:
        print('ERROR: Forbidden::autoindex')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # ssl_offload
    if 'ssl_offload' in form.keys():
        ssl_offload = form.getvalue('ssl_offload')
        yaml_parsed_profileyaml['ssl_offload'] = ssl_offload
    else:
        print('ERROR: Forbidden::ssl_offload')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # pagespeed
    if 'pagespeed' in form.keys():
        pagespeed = form.getvalue('pagespeed')
        yaml_parsed_profileyaml['pagespeed'] = pagespeed
    else:
        print('ERROR: Forbidden::pagespeed')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # pagespeed_filter
    if 'pagespeed_filter' in form.keys():
        pagespeed_filter = form.getvalue('pagespeed_filter')
        yaml_parsed_profileyaml['pagespeed_filter'] = pagespeed_filter
    else:
        print('ERROR: Forbidden::pagespeed_filter')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # brotli
    if 'brotli' in form.keys():
        brotli = form.getvalue('brotli')
        yaml_parsed_profileyaml['brotli'] = brotli
    else:
        print('ERROR: Forbidden::brotli')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # gzip
    if 'gzip' in form.keys():
        gzip = form.getvalue('gzip')
        yaml_parsed_profileyaml['gzip'] = gzip
    else:
        print('ERROR: Forbidden::gzip')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # http2
    if 'http2' in form.keys():
        http2 = form.getvalue('http2')
        yaml_parsed_profileyaml['http2'] = http2
    else:
        print('ERROR: Forbidden::http2')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # access_log
    if 'access_log' in form.keys():
        access_log = form.getvalue('access_log')
        yaml_parsed_profileyaml['access_log'] = access_log
    else:
        print('ERROR: Forbidden::access_log')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # open_file_cache
    if 'open_file_cache' in form.keys():
        open_file_cache = form.getvalue('open_file_cache')
        yaml_parsed_profileyaml['open_file_cache'] = open_file_cache
    else:
        print('ERROR: Forbidden::open_file_cache')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # clickjacking_protect
    if 'clickjacking_protect' in form.keys():
        clickjacking_protect = form.getvalue('clickjacking_protect')
        yaml_parsed_profileyaml['clickjacking_protect'] = clickjacking_protect
    else:
        print('ERROR: Forbidden::clickjacking_protect')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # disable_contenttype_sniffing
    if 'disable_contenttype_sniffing' in form.keys():
        disable_contenttype_sniffing = form.getvalue('disable_contenttype_sniffing')
        yaml_parsed_profileyaml['disable_contenttype_sniffing'] = disable_contenttype_sniffing
    else:
        print('ERROR: Forbidden::disable_contenttype_sniffing')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # xss_filter
    if 'xss_filter' in form.keys():
        xss_filter = form.getvalue('xss_filter')
        yaml_parsed_profileyaml['xss_filter'] = xss_filter
    else:
        print('ERROR: Forbidden::xss_filter')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # hsts
    if 'hsts' in form.keys():
        hsts = form.getvalue('hsts')
        yaml_parsed_profileyaml['hsts'] = hsts
    else:
        print('ERROR: Forbidden::hsts')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # dos_mitigate
    if 'dos_mitigate' in form.keys():
        dos_mitigate = form.getvalue('dos_mitigate')
        yaml_parsed_profileyaml['dos_mitigate'] = dos_mitigate
    else:
        print('ERROR: Forbidden::dos_mitigate')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # test_cookie
    if 'test_cookie' in form.keys():
        test_cookie = form.getvalue('test_cookie')
        yaml_parsed_profileyaml['test_cookie'] = test_cookie
    else:
        print('ERROR: Forbidden::test_cookie')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # symlink_protection
    if 'symlink_protection' in form.keys():
        symlink_protection = form.getvalue('symlink_protection')
        yaml_parsed_profileyaml['symlink_protection'] = symlink_protection
    else:
        print('ERROR: Forbidden::symlink_protection')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # redirect_to_ssl
    if 'redirect_to_ssl' in form.keys():
        redirect_to_ssl = form.getvalue('redirect_to_ssl')
        yaml_parsed_profileyaml['redirect_to_ssl'] = redirect_to_ssl
    else:
        print('ERROR: Forbidden::redirect_to_ssl')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # redirect_aliases
    if 'redirect_aliases' in form.keys():
        redirect_aliases = form.getvalue('redirect_aliases')
        yaml_parsed_profileyaml['redirect_aliases'] = redirect_aliases
    else:
        print('ERROR: Forbidden::redirect_aliases')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # wwwredirect
    if 'wwwredirect' in form.keys():
        wwwredirect = form.getvalue('wwwredirect')
        yaml_parsed_profileyaml['wwwredirect'] = wwwredirect
    else:
        print('ERROR: Forbidden::wwwredirect')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # redirectstatus
    if 'redirectstatus' in form.keys():
        redirectstatus = form.getvalue('redirectstatus')
        yaml_parsed_profileyaml['redirectstatus'] = redirectstatus
    else:
        print('ERROR: Forbidden::redirectstatus')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    # redirecturl
    if redirectstatus != "none":
        if 'redirecturl' in form.keys():
            redirecturl = form.getvalue('redirecturl')
            if not redirecturl == "noredirection":
                regex = re.compile(
                    r'^(?:http|ftp)s?://'
                    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
                    r'localhost|'
                    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                    r'(?::\d+)?'
                    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
                it_matches = regex.match(redirecturl)
                if not it_matches:
                    print('ERROR: Invalid Redirect URL. The URL must be something like https://google.com ')
                    print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
                    print('</div>')
                    print('</div>')
                    print('</div>')
                    print('</body>')
                    print('</html>')
                    sys.exit(0)
                else:
                    yaml_parsed_profileyaml['redirecturl'] = redirecturl
            else:
                yaml_parsed_profileyaml['redirecturl'] = current_redirecturl
    # append_requesturi
    if 'append_requesturi' in form.keys():
        append_requesturi = form.getvalue('append_requesturi')
        yaml_parsed_profileyaml['append_requesturi'] = append_requesturi
    else:
        print('ERROR: Forbidden::append_requesturi')
        print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
        print('</div>')
        print('</div>')
        print('</div>')
        print('</body>')
        print('</html>')
        sys.exit(0)
    print('<div class="panel panel-default">')
    print(('<div class="panel-heading"><h3 class="panel-title">Package: <strong>'+form.getvalue('cpanelpkg')+'</strong></h3></div>'))
    print(('<div class="panel-body">'))
    with open(pkgdomaindata, 'w') as yaml_file:
        yaml.dump(yaml_parsed_profileyaml, yaml_file, default_flow_style=False)
    print('<div class="icon-box">')
    print('<span class="glyphicon glyphicon-thumbs-up" aria-hidden="true"></span> Server Settings updated')
    print('</div>')
    print('</div>')
    print('</div>')
else:
        print('<div class="alert alert-info"><span class="glyphicon glyphicon-alert" aria-hidden="true"></span> Forbidden </div>')
print('<div class="panel-footer"><small><a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">&#8734; A U T O M 8 N</a></small></div>')
print('</div>')  # marker3
print('</div>')  # marker2
print('</body>')
print('</html>')
