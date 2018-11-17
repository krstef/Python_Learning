import time
from datetime import datetime as dt
host_path = "/etc/hosts"
#host_path = "hosts"
redirect = "127.0.0.1"

website_list=["www.facebook.com", "facebook.com", "www.hollisterco.com", "hollisterco.com"]

while 1:
    """ if we are in working time, open hosts file
        if hosts doesn't contain blocked web sites,
            add them, otherwise pass
    """
    """ if we are not in working time, open hosts file
        if host contain blocked web sites, ignore them
        otherwise
    """
    if dt(dt.now().year, dt.now().month, dt.now().day,16) < dt.now() < \
        dt(dt.now().year, dt.now().month, dt.now().day,17):
            with open(host_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        #pass is equal to continue in C
                        pass
                    else:
                        file.write(redirect + " " + website +"\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
    time.sleep(5)
