from prometheus_client import start_http_server, Gauge, Info
import time
import requests

packets_mixed_total = Gauge('nym_packets_mixed_total', 'Packets mixed since startup')
packets_mixed_last = Gauge('nym_packets_mixed_last', 'Packets mixed in last 30 seconds')

meta = Info('nym_meta', 'Information about node')


def get_metrics(mixer_ip):
    stats = requests.get(f'http://{mixer_ip}:8000/stats').json()
    info = requests.get(f'https://nodes.guru/api/nym/mixnode?q={mixer_ip}&limit=6').json()

    total_mixed = stats['packets_sent_since_startup']
    current_mixed = stats['packets_sent_since_last_update']

    packets_mixed_total.set(total_mixed)
    packets_mixed_last.set(current_mixed)
    meta.info({k: str(v) for k, v in info['metrics'].items()})


if __name__ == '__main__':
    ip = requests.get('https://api.ipify.org').text
    start_http_server(8991)
    while True:
        get_metrics(ip)
        time.sleep(30)
