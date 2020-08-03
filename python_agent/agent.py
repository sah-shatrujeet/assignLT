#!/usr/bin/env python3

import os
import subprocess
import shutil
import socket
import json

def get_stats():
    stats = {}

    cpu_load = [x / os.cpu_count() * 100 for x in os.getloadavg()][1]
    stats['cpu_load'] = round(cpu_load)

    mem = subprocess.run(['free'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    res = mem.split()
    # print(mem)
    # print(str(res))
    total_ram = round(int(res[7])/(1024 * 1024))
    used_ram = round(int(res[8])/(1024 * 1024))
    free_ram = round(int(res[9])/(1024 * 1024))
    cache = round(int(res[11])/(1024 * 1024))
    # print(total_ram)
    stats['ram'] = dict({
        'total_ram': total_ram,
        'used_ram': used_ram,
        'free_ram': free_ram,
        'buff/cache': cache
    })

    # print(shutil.disk_usage("/"))
    total, used, free = shutil.disk_usage("/")
    stats['disk'] = dict(
    {
        'total_disk_space': round(total / (1024 * 1024 * 1024), 1),
        'used_disk_space': round(used / (1024 * 1024 * 1024), 1),
        'free_disk_space': round(free / (1024 * 1024 * 1024), 1)
    })

    return stats

####### send data to Logstash. verify your host and port #######   
def send_to_logstash(dictdoc, host, port):
    print("Send_to_logstash: ", dictdoc)
    # Attach Logstash TCP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    try:
        # Send to Logstash
        str_entry = json.dumps(dictdoc)
        result = s.send((str_entry + "\n").encode("UTF-8"))

    except Exception as e:
        # Logs through the socket the error
        err_message = 'Error parsing the object. Exception: {}'.format(str(e))
        send_entry(s, err_message)
        raise e

    finally:
        s.close()

    return

if __name__ == "__main__":
    stats = get_stats()
    # print(stats)
    send_to_logstash(stats, "100.26.174.81", 5400)
