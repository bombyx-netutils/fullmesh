#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

import os


class BymConst:

    libDir = "/usr/lib/bombyx-mesh"
    etcDir = "/etc/bombyx-mesh"
    varDir = "/var/bombyx-mesh"
    runDir = "/run/bombyx-mesh"
    logDir = "/var/log/bombyx-mesh"
    tmpDir = "/tmp/bombyx-mesh"

    pidFile = os.path.join(runDir, "bombyx-mesh.pid")


class BymParam:

    def __init__(self):
        self.logLevel = None
        self.abortOnError = False

        self.dbusMainObject = None
        self.config = None
        self.trafficManager = None
        self.connectionManager = None
        self.daemon = None
