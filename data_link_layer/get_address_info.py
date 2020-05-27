import psutil

info = psutil.net_if_addrs()
address = info['WLAN'][0].address
print(info)
print(address)