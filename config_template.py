import os
basedir = os.path.abspath(os.path.dirname(__file__))

# BASIC APP CONFIG
WTF_CSRF_ENABLED = True
SECRET_KEY = 'We are the world'
BIND_ADDRESS = '127.0.0.1'
PORT = 9393
LOGIN_TITLE = "PDNS"

# TIMEOUT - for large zones
TIMEOUT = 10

# LOG CONFIG
LOG_LEVEL = 'DEBUG'
LOG_FILE = 'logfile.log'

# Upload
UPLOAD_DIR = os.path.join(basedir, 'upload')

# DATABASE CONFIG
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@192.168.59.103/pdns'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# LDAP CONFIG
LDAP_TYPE = 'ldap' # use 'ad' for MS Active Directory
LDAP_URI = 'ldaps://your-ldap-server:636'
LDAP_USERNAME = 'cn=dnsuser,ou=users,ou=services,dc=duykhanh,dc=me'
LDAP_PASSWORD = 'dnsuser'
LDAP_SEARCH_BASE = 'ou=System Admins,ou=People,dc=duykhanh,dc=me'
# Additional options only if LDAP_TYPE=ldap
LDAP_USERNAMEFIELD = 'uid'
LDAP_FILTER = '(objectClass=inetorgperson)'

# Github Oauth
GITHUB_OAUTH_ENABLE = True
GITHUB_OAUTH_KEY = 'G0j1Q15aRsn36B3aD6nwKLiYbeirrUPU8nDd1wOC'
GITHUB_OAUTH_SECRET = '0WYrKWePeBDkxlezzhFbDn1PBnCwEa0vCwVFvy6iLtgePlpT7WfUlAa9sZgm'
GITHUB_OAUTH_SCOPE = 'email'
GITHUB_OAUTH_URL = 'http://127.0.0.1:5000/api/v3/'
GITHUB_OAUTH_TOKEN = 'http://127.0.0.1:5000/oauth/token'
GITHUB_OAUTH_AUTHORIZE = 'http://127.0.0.1:5000/oauth/authorize'

#Default Auth
BASIC_ENABLED = True
SIGNUP_ENABLED = True

# POWERDNS CONFIG
PDNS_STATS_URL = 'http://172.16.214.131:8081/'
PDNS_API_KEY = 'you never know'
PDNS_VERSION = '3.4.7'

# RECORDS ALLOWED TO EDIT
RECORDS_ALLOW_EDIT = ['A', 'AAAA', 'CNAME', 'SPF', 'PTR', 'MX', 'TXT']
