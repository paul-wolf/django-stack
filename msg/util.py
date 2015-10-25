import re
from . models import *

email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    # quoted-string, see also http://tools.ietf.org/html/rfc2822#section-3.2.5
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"'
    r')@((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)$)'  # domain
    r'|\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]$', re.IGNORECASE)  

# literal form, ipv4 address (SMTP 4.1.3)

def valid_email(email):
    """Check if email is valid.

    This only check that it is is ietf conformant, not that it exists somewhere.

    """
    return email_re.match(email)

def generate_username(email):
    """Generate a user name from an email.

    """
    parts = email.split('@')
    username = ''
    if len(parts) == 0:
        username= "user"
    else:
        username = parts[0]

    username_max_length = User._meta.get_field('username').max_length
    if len(username) > username_max_length:
        username = username[:username_max_length-4] # make room as well for adding an integer value

    # now check that it's unique
    username_tmp = username
    for i in range(1000):
        users = User.objects.filter(username=username_tmp)
        if not users:
            username = username_tmp
            break
        else:
            # bad: someone has that username already
            username_tmp = username+str(i)

    return username

def admin_notification(subject,message):
    """Email to super users.

    """
    try:
        # use email provider for this
        #for admin in ADMINS:
        #    mailgun.send_message(admin[1],subject,message,DEFAULT_FROM_EMAIL)
        pass
    except Exception as e:
        logger.exception(e)
