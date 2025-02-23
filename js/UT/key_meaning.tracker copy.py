# UT.js Manual
# Tracker for ctforion.com
# Developed by: Unkn0wn2603
# Description:
#   This file defines the constants and keyword rules used by UT.js.
#   UT.js is a tracking solution designed to monitor performance
#   and capture event data efficiently for ctforion.com.
# Creation Date: January 26, 2025


UT_KEY = { 
    "ACTIVITY_TYPE" : {
        "0"  : "end",
        "1"  : "start",
        "c"  : "click",
        "d"  : "download",
        "e"  : "error",
        "f"  : "focus",
        "h"  : "hover",
        "i"  : "idle",
        "r"  : "reconnect",
        "s"  : "scroll",
        "u"  : "upload",
        "v"  : "visibility",
        "lt" : "load_time",
        "fc" : "focus_change",
        "vc" : "visibility_change",
        "fs" : "form_submit",
        "is" : "idle_start",
        "ie" : "idle_end",
        "id" : "input_data",
        "ic" : "input_complete",
        "kp" : "key_press",
        "po" : "page_open",
        "pc" : "page_close",
        "er" : "error_reject",
        "do" : "device_orientation",
        "dm" : "device_motion",
    },
    
    "CONTENT_VALUE_TYPE" : {
        "0"       : False,
        "1"       : True,
        
        "T"       : True,
        "F"       : False,
        
        "visible" : True,
        "hidden"  : False,
        
        "N"       : None, 
        "O"       : None,
        "E"       : "",
        
        
    },
    "CONTENT_TYPE" : { 
        # those things accessable jsonbody["D"]...
        "0"   : "things_are_endings",
        "1"   : "things_are_starting",
        
        # CHAPITAL SINGLE LETTERED KEYS ARE USED FOR TRACKING
        "D"   : "data",
        "M"   : "message",
        "N"   : "filename",
        "S"   : "source",
        "T"   : "time",
        "U"   : "URL",
        "R"   : "referrer_url",
        "E"   : "element",
        "I"   : "id",
        "K"   : "key",
        "V"   : "value",
        "O"   : "opening",
        "C"   : "closing",
        
        # SMALL SINGLE LETTERED KEYS ARE USED FOR TRACKING
        "a"   : "alpha",
        "b"   : "beta",
        "g"   : "gamma",
        
        # SMALL DOUBLE LETTERED KEYS ARE USED FOR TRACKING
        "cc"  : "click_count",
        "et"  : "element_type",
        
        
        "oX"  : "orientation_x",
        "oY"  : "orientation_y",
        "oZ"  : "orientation_z",
        "aX"  : "acceleration_x",
        "aY"  : "acceleration_y",
        "aZ"  : "acceleration_z",
        "rA"  : "rotation_alpha",
        "rB"  : "rotation_beta",
        "rG"  : "rotation_gamma",
        
        "st"  : "status",
        "ec"  : "event_code",
        "pt"  : "page_title",
        "ln"  : "line",
        "cl"  : "column",
        "st"  : "stack",
        "fn"  : "filename",
        "ft"  : "filetype",
        "rs"  : "reason",
        "fi"  : "form_id",
        
        # SMALL TRIPLE LETTERED KEYS ARE USED FOR TRACKING
        
        "elt" : "element_text",
        "elh" : "element_html",
        "elc" : "element_class",
        "elh" : "element_href",
        "els" : "element_src",
        "elv" : "element_value",


        "sdp" : "scroll_depth",
        "sdr" : "scroll_direction",
        "scp" : "scroll_position",
        "plt" : "page_load_time",
        "idt" : "idle_duration_time",
        "lcf" : "largestcontentfulpaint", # THIS PRESENTS LARGE CONTENTFUL PAINT
        "nvs" : "navigationStart",        # THIS PRESENTS NAVIGATION STARTIN
        "cle" : "domContentLoadedEventEnd",
        "lee" : "loadEventEnd",
        "fpt" : "firstPaint",
        "fcp" : "firstContentfulPaint",
        "trc" : "totalResource",
        "rlt" : "totalResourceLoadTime",
    }
}





























# IP_V4_TOTAL_STORAGE = 0
# total_part = 4
# part_size = 3
# total_dot = 3
# one_ip = (total_part * part_size) + total_dot
# # combination_count = 256 ** 4
# combination_count = 4294967296
# IP_V4_TOTAL_STORAGE = one_ip * combination_count
# # convert it into GB
# IP_V4_TOTAL_STORAGE = IP_V4_TOTAL_STORAGE / (1024 ** 3)
# # print(IP_V4_TOTAL_STORAGE)
# x = 16777216+1048576+65536+4194304+16777216+65536+268435456+268435456


# # total ip address:                   4294967296
# # depertable ip address:              -575799296
# # ----------------------------------------------
# # total ip address after deperting:   3719168000
# deperted_ip = 3719168000
# deperted_storage = deperted_ip * one_ip
# deperted_storage = deperted_storage / (1024 ** 3)
# # print(deperted_storage)


























































# from threading import Thread
# from queue import Queue
# import json
# import requests
# import os

# print("\n******************************************************")
# print("*                                                    *")
# print("*  __  __ _____  _____ _                             *")
# print("* |  \\/  |  __ \\|_   _| |                            *")
# print("* | \\  / | |__) | | | | |                            *")
# print("* | |\\/| |  _  /  | | | |                            *")
# print("* | |  | | | \\ \\ _| |_| |____                        *")
# print("* |_|  |_|_|  \\_\\_____|______|                       *")
# print("*                                                    *")
# print("* Mass Reverse IP Lookup                             *")
# print("* Coded by thebish0p                                 *")
# print("* https://github.com/thebish0p/                      *")
# print("******************************************************\n")

# INPUT_HANDLE=input('[*] Enter ip addresses file: ')
# OUTPUT_HANDLE = open('output.txt', 'a')

# addresses = [account.rstrip() for account in open(INPUT_HANDLE.strip()).readlines()]
# THREADS =int(input("[*] Enter number of threads: "))

# address_q = Queue()
# for addy in addresses:
#     address_q.put(addy)
# class ReverseIP(Thread):
#     def __init__(self, address_q):
#         self.address_q = address_q
#         Thread.__init__(self)

#     def run(self):
#         while not self.address_q.empty():
#             ipaddy = self.address_q.get()
#             self.address_q.task_done()
#             s = requests.Session()
#             try:
#                 print(f"[*] Reversing {ipaddy} ...")
#                 s.headers.update({
#                     'authority': 'domains.yougetsignal.com',
#                     'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
#                     'x-prototype-version': '1.6.0',
#                     'x-requested-with': 'XMLHttpRequest',
#                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#                     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#                     'origin': 'https://www.yougetsignal.com',
#                     'sec-fetch-site': 'same-site',
#                     'sec-fetch-mode': 'cors',
#                     'sec-fetch-dest': 'empty',
#                     'referer': 'https://www.yougetsignal.com/tools/web-sites-on-web-server/',
#                     'accept-language': 'en-US,en;q=0.9,ar;q=0.8,fr;q=0.7',
#                 })

#                 data = {
#                   'remoteAddress': ipaddy,
#                   'key': '',
#                   '_': ''
#                 }

#                 response = s.post('https://domains.yougetsignal.com/domains.php', data=data)

#                 if '{"status":"Fail"' in response.text:
#                     print('[*] Limit reached change your IP!')
#                     exit()
#                 try:
#                     loaded_json=(json.loads(response.text)['domainArray'])
#                 except:
#                     print(f"[*] No domains found for {ipaddy}")
#                     return
#                 OUTPUT_HANDLE.write('Results for '+ipaddy+' :\n')
#                 print(f"[*] {len(loaded_json)} domains found for {ipaddy}")
#                 for i in range(len(loaded_json)):
#                     OUTPUT_HANDLE.write(loaded_json[i][0]+'\n')
#                     OUTPUT_HANDLE.flush()
#                 OUTPUT_HANDLE.write('=================================================\n')



#             except Exception as e:
#                 print(e)

# threads = []
# for j in range(THREADS):
#     threads.append(ReverseIP(address_q))
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()

# print("******************************************************")
# print('[*] Scan is done')
# print(f'[*] Output file: {os.getcwd()}/output.txt')
# print("******************************************************")
















# import argparse
# import socket
# import sys
# import threading
# from threading import Thread
# import queue

# # Default DNS resolvers
# DEFAULT_RESOLVERS = [
#     "1.1.1.1", "1.0.0.1", "8.8.8.8", "8.8.4.4", "9.9.9.9", "149.112.112.112",
#     "208.67.222.222", "208.67.220.220", "64.6.64.6", "64.6.65.6", "198.101.242.72",
#     "8.26.56.26", "8.20.247.20", "185.228.168.9", "185.228.169.9",
#     "76.76.19.19", "76.223.122.150", "94.140.14.14", "94.140.15.15",
# ]
# def load_resolvers_from_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             return [line.strip() for line in file if line.strip()]
#     except IOError as e:
#         print(f"Failed to open resolvers file: {e}", file=sys.stderr)
#         sys.exit(1)

# def resolve_ip(ip, resolvers, protocol, port, domain_only):
#     for resolver_ip in resolvers:
#         try:
#             addr_info = socket.getaddrinfo(resolver_ip, port, proto=socket.IPPROTO_TCP if protocol == 'tcp' else socket.IPPROTO_UDP)
#             for family, socktype, proto, canonname, sockaddr in addr_info:
#                 with socket.socket(family, socktype, proto) as s:
#                     s.settimeout(5)
#                     s.connect(sockaddr)
#                     s.sendall(build_dns_query(ip))
#                     response = s.recv(512)
#                     domains = parse_dns_response(response)
#                     for d in domains:
#                         if domain_only:
#                             print(d)
#                         else:
#                             print(f"{ip}\t{d}")
#                     return
#         except Exception:
#             continue
#     print(f"Failed to resolve IP: {ip}", file=sys.stderr)

# def build_dns_query(ip):
#     # Construct a DNS query for PTR record
#     parts = ip.split('.')
#     reverse_ip = '.'.join(reversed(parts)) + '.in-addr.arpa'
#     query = b'\x12\x34'  # Transaction ID
#     query += b'\x01\x00'  # Standard query
#     query += b'\x00\x01'  # Questions: 1
#     query += b'\x00\x00'  # Answer RRs: 0
#     query += b'\x00\x00'  # Authority RRs: 0
#     query += b'\x00\x00'  # Additional RRs: 0
#     for part in reverse_ip.split('.'):
#         query += bytes([len(part)])
#         query += part.encode()
#     query += b'\x00'  # End of domain name
#     query += b'\x00\x0c'  # Type: PTR
#     query += b'\x00\x01'  # Class: IN
#     return query

# def parse_dns_response(response):
#     # Simplified DNS response parser for PTR records
#     if len(response) < 12:
#         return []
#     qdcount = int.from_bytes(response[4:6], 'big')
#     ancount = int.from_bytes(response[6:8], 'big')
#     offset = 12
#     for _ in range(qdcount):
#         while response[offset] != 0:
#             offset += response[offset] + 1
#         offset += 5
#     domains = []
#     for _ in range(ancount):
#         while response[offset] != 0:
#             offset += response[offset] + 1
#         offset += 10
#         rdlength = int.from_bytes(response[offset:offset+2], 'big')
#         offset += 2
#         domain = []
#         end = offset + rdlength
#         while offset < end:
#             length = response[offset]
#             if length == 0:
#                 break
#             domain.append(response[offset+1:offset+1+length].decode())
#             offset += length + 1
#         domains.append('.'.join(domain))
#     return domains

# def worker(work_queue, resolvers, protocol, port, domain_only):
#     while True:
#         ip = work_queue.get()
#         if ip is None:
#             break
#         resolve_ip(ip, resolvers, protocol, port, domain_only)
#         work_queue.task_done()

# def main():
#     resolvers = []
#     resolvers.extend(DEFAULT_RESOLVERS)
#     total_threads = 10
#     protocols = ['tcp', 'udp']
#     protocol = 'udp'
#     port = 53
#     only_print_domains = False

#     if not resolvers:
#         print("No DNS resolvers specified.", file=sys.stderr)
#         sys.exit(1)

#     work_queue = queue.Queue()
#     threads = []
#     for _ in range(total_threads):
#         t = threading.Thread(target=worker, args=(work_queue, resolvers, protocol, port, only_print_domains))
#         t.start()
#         threads.append(t)

#     try:
#         for line in sys.stdin:
#             work_queue.put(line.strip())
#     except KeyboardInterrupt:
#         pass

#     work_queue.join()

#     for _ in range(total_threads):
#         work_queue.put(None)
#     for t in threads:
#         t.join()

# if __name__ == "__main__":
#     main()



























import argparse
import socket
import sys

# Default DNS resolvers
DEFAULT_RESOLVERS = [
    "1.1.1.1", "1.0.0.1", "8.8.8.8", "8.8.4.4", "9.9.9.9", "149.112.112.112",
    "208.67.222.222", "208.67.220.220", "64.6.64.6", "64.6.65.6", "198.101.242.72",
    "8.26.56.26", "8.20.247.20", "185.228.168.9", "185.228.169.9",
    "76.76.19.19", "76.223.122.150", "94.140.14.14", "94.140.15.15",
]

def load_resolvers_from_file(file_path):
    print(f"Loading resolvers from file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            resolvers = [line.strip() for line in file if line.strip()]
            print(f"Loaded resolvers: {resolvers}")
            return resolvers
    except IOError as e:
        print(f"Failed to open resolvers file: {e}", file=sys.stderr)
        sys.exit(1)

def resolve_ip(ip, resolvers, protocol, port, domain_only):
    print(f"Resolving IP: {ip}")
    for resolver_ip in resolvers:
        print(f"Using resolver: {resolver_ip}")
        try:
            addr_info = socket.getaddrinfo(
                resolver_ip, port,
                proto=socket.IPPROTO_TCP if protocol == 'tcp' else socket.IPPROTO_UDP
            )
            for family, socktype, proto, canonname, sockaddr in addr_info:
                print(f"Connecting to {sockaddr}")
                with socket.socket(family, socktype, proto) as s:
                    s.settimeout(5)
                    s.connect(sockaddr)
                    query = build_dns_query(ip)
                    print(f"Sending DNS query: {query}")
                    s.sendall(query)
                    response = s.recv(512)
                    print(f"Received response: {response}")
                    domains = parse_dns_response(response)
                    for d in domains:
                        if domain_only:
                            print(d)
                        else:
                            print(f"{ip}\t{d}")
                    return
        except Exception as e:
            print(f"Error resolving {ip} with resolver {resolver_ip}: {e}", file=sys.stderr)
            continue
    print(f"Failed to resolve IP: {ip}", file=sys.stderr)

def build_dns_query(ip):
    print(f"Building DNS query for IP: {ip}")
    parts = ip.split('.')
    reverse_ip = '.'.join(reversed(parts)) + '.in-addr.arpa'
    query = b'\x12\x34'  # Transaction ID
    query += b'\x01\x00'  # Standard query
    query += b'\x00\x01'  # Questions: 1
    query += b'\x00\x00'  # Answer RRs: 0
    query += b'\x00\x00'  # Authority RRs: 0
    query += b'\x00\x00'  # Additional RRs: 0
    for part in reverse_ip.split('.'):
        query += bytes([len(part)])
        query += part.encode()
    query += b'\x00'  # End of domain name
    query += b'\x00\x0c'  # Type: PTR
    query += b'\x00\x01'  # Class: IN
    print(f"Constructed DNS query: {query}")
    return query

def parse_dns_response(response):
    print(f"Parsing DNS response")
    if len(response) < 12:
        print("Response too short to parse.")
        return []
    qdcount = int.from_bytes(response[4:6], 'big')
    ancount = int.from_bytes(response[6:8], 'big')
    offset = 12
    for _ in range(qdcount):
        while response[offset] != 0:
            offset += response[offset] + 1
        offset += 5
    domains = []
    for _ in range(ancount):
        while response[offset] != 0:
            offset += response[offset] + 1
        offset += 10
        rdlength = int.from_bytes(response[offset:offset+2], 'big')
        offset += 2
        domain = []
        end = offset + rdlength
        while offset < end:
            length = response[offset]
            if length == 0:
                break
            domain.append(response[offset+1:offset+1+length].decode())
            offset += length + 1
        domains.append('.'.join(domain))
    print(f"Extracted domains: {domains}")
    return domains

def main():
    print("Starting main function")
    resolvers = DEFAULT_RESOLVERS
    protocol = 'udp'
    port = 53
    only_print_domains = False

    if not resolvers:
        print("No DNS resolvers specified.", file=sys.stderr)
        sys.exit(1)

    try:
        with open("ip", 'r') as file:
            print("Reading IP addresses from file")
            for line in file.readlines():
                print(f"Processing line: {line}")
                ip = line.strip()
                if ip:
                    resolve_ip(ip, resolvers, protocol, port, only_print_domains)
    except KeyboardInterrupt:
        print("Process interrupted by user.")

if __name__ == "__main__":
    main()
