# prometheus-nym

Simple Prometheus exporter for Nym mixnodes, written in Python.

## Oneliner

```bash
git clone https://github.com/BakasaRus/prometheus-nym.git && cd ./prometheus-nym/ && bash ./install.sh <PORT>
```

You can specify port for exposing metrics or leave it empty for default port (8991).

You'll need superuser rights to install Python packages.

## Uninstall

```bash
sudo systemctl stop nym-exporter && sudo systemctl disable nym-exporter && rm -rf ${installment_dir}/prometheus-nym && sudo rm /etc/systemd/system/nym-exporter.service
```

## Acknowledgments

Thanks to [Nym project](https://nymtech.net/) for wonderful project and [NodesGuru team](https://nodes.guru/) for easy-to-use Nym API.