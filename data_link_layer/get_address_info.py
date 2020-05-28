import psutil
from scapy.all import srp, Ether, ARP, conf, sr, IP, ICMP
from concurrent.futures.thread import ThreadPoolExecutor

# 获取本机mac地址
info = psutil.net_if_addrs()
address = info['WLAN'][0].address
# print(info)
# print(address)

# 获取局域网电脑mac地址
conf.verb = 0
def handle_arp_address(ip_address):
    """
    srp,让arp数据包工作在数据帧，也就是数据链路层上，发送数据帧
    Ether工作在以太网，局域网中
    dst是目的广播mac地址，pdst,是目的IP地址
    :param ip_address:
    :return:
    """
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address), timeout=2)
    for snd, rcv in ans:
        rcv.sprintf(r"%Ether.src% & %ARP.psrc%")
        # print(rcv.sprintf(r"%Ether.src% & %ARP.psrc%"))

# handle_arp_address("192.168.0.1")

ip_list = ["192.168.0." + str(i) for i in range(1, 255)]
t = ThreadPoolExecutor()
thread_list = []
for ip in ip_list:
    thread = t.submit(handle_arp_address, ip)
    thread_list.append(thread)
t.shutdown()

# 发送请求包
def handle_alive(ip):
    """
    srp,让arp数据包工作在数据帧，也就是数据链路层上，发送数据帧
    sr真实让ICPM协议工作在网络层上，发送的是数据包
    :param ip:
    :return:
    """
    ans,unans = sr(IP(dst=ip)/ICMP(), retry=0, timeout=2)
    for snd, rcv in ans:
        print(rcv.sprintf(r"%IP.src% is alive"))

# handle_alive('192.168.0.1')

n = ThreadPoolExecutor(50)
n_list = []
for ip in ip_list:
    td = n.submit(handle_alive, ip)
    n_list.append(td)
n.shutdown()
