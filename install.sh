#!/usr/bin/env bash

sudo apt install -y python3.9 python3.9-venv

python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cur_dir=$(pwd)
port=$1

sudo tee << EOF > /dev/null /etc/systemd/system/nym-exporter.service
[Unit]
Description=Nym exporter for Prometheus

[Service]
User=$USER
Type=simple
ExecStart=$cur_dir/.venv/bin/python $cur_dir/main.py $port
Restart=on-failure
RestartSec=10s

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl start nym-exporter
sudo systemctl enable nym-exporter

echo "Success! Now you can look at your metrics at port $port. Don't forget to add them to Prometheus"