#!/usr/bin/env python

import re
from tomcat import Tomcat, TomcatCluster, parse_warfile
import time
import logging

def cluster_deploy(cluster, webapp_list, interval=20, timeout=40):

    def is_started(warFile):
        context = parse_warfile(warFile)
        print "CONTEXT: " + str(context[0])
        for k, v in cluster.webapp_status().iteritems():
            print "KEY: " + str(k)
            print "VALUE: " + str(v)
            if k == context[0] and v{} == "STARTED":
                return True
        return False


    deploy_results = {}
    counter = 0

    for warFile in webapp_list:
        deploy_results = cluster.run_command("deploy", warFile)

    if is_started(warFile) == True:
        print "all apps successfully deployed"
        exit(0)
    else:
        while counter != timeout and is_started(warFile) == False:

                time.sleep(interval)
                print cluster.webapp_status()
                print "Application still starting"
                counter += 20
                print "COUNTER: " + str(counter)
                if counter == timeout:
                    print "Deployment failed"
                    exit(20)


def main():
    #print "Find pools over 50: " + str(t.find_pools_over(50))
    #print "Check memory" + str(t.check_memory(50))

    #t.undeploy_old_versions(vhost=?)
    #t.deploy(something.zip,/tmp,vhost=?)

    c = TomcatCluster('192.168.50.10', 'admin', 'admin')

    cluster_deploy(c, ["/tmp/shit.war"])



if __name__ == "__main__":
    main()
