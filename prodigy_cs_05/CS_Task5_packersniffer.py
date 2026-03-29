from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if protocol == 6:  # TCP
            if TCP in packet:
                sport = packet[TCP].sport
                dport = packet[TCP].dport
                print(f"TCP Packet: {ip_src}:{sport} -> {ip_dst}:{dport}")

        elif protocol == 17:  # UDP
            if UDP in packet:
                sport = packet[UDP].sport
                dport = packet[UDP].dport
                print(f"UDP Packet: {ip_src}:{sport} -> {ip_dst}:{dport}")

        else:
            print(f"Other IP Packet: {ip_src} -> {ip_dst} (Protocol: {protocol})")

def main():
    # Sniff packets with a filter (in this case, IP packets only)
    sniff(filter="ip", prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
