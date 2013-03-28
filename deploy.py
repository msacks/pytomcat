#!/usr/bin/env python

import re
from tomcat import Tomcat

def main():
    t = Tomcat('192.168.50.10', 'admin', 'admin')
    print t.find_pools_over(1)
    print t.check_memory(1)

    #t.undeploy_old_versions(vhost=?)
    #t.deploy(something.zip,/tmp,vhost=?)

if __name__ == "__main__":
    main()
