#!/usr/bin/env python

import re
from tomcat import Tomcat, TomcatCluster
import time
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('main: This message should go to the log file')


def cluster_deploy(cluster, webapp_list, interval=20, timeout=300):
    deploy_results = {}

    for warFile in webapp_list:
        deploy_results = cluster.run_command("deploy", warFile)

    for k, v in cluster.list_webapps().iteritems():
        if v == "STARTED":
            print "all apps successfully deployed"
            exit(0)
        else:
            while interval != timeout:
                for k,v in cluster.list_webapps().iteritems():
                    if v != "STARTED":
                        print "apps haven't started yet, waiting 10 seconds"
                        time.sleep(10)
                    interval += 1


def main():
    #print "Find pools over 50: " + str(t.find_pools_over(50))
    #print "Check memory" + str(t.check_memory(50))

    #t.undeploy_old_versions(vhost=?)
    #t.deploy(something.zip,/tmp,vhost=?)

    c = TomcatCluster('192.168.50.10', 'admin', 'admin')

    cluster_deploy(c, ["/tmp/shit.war"])



if __name__ == "__main__":
    main()
