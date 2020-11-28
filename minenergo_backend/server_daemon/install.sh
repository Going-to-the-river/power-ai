#!/bin/bash

cd ..

#~~~~~~~~~~VARIABLES~~~~~~~~~~~~~
WD=$(pwd)
USER=$(whoami)
SERVICE_NAME="minenergo_backend.service"
PYTHON="${WD}/venv/bin/python"

#~~~~~~~~~create main daemon~~~~~~~~~~~

EXEC_START="${PYTHON} ${WD}/server.py"

echo "[Service]

Type=simple

WorkingDirectory=${WD}/server_daemon
User=${USER}
Group=${USER}

ExecStart=${EXEC_START}
# ExecStop=
ExecReload=${EXEC_START}

PIDFile=/tmp/${SERVICE_NAME}.pid
Restart=always
RestartSec=30

[Install]

WantedBy=multi-user.target" > /etc/systemd/system/${SERVICE_NAME}

systemctl daemon-reload
systemctl enable ${SERVICE_NAME}

echo Service enabled. To start service Type "sudo systemctl start ${SERVICE_NAME}" or reboot.
