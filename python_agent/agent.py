#!/usr/bin/env python3

import os

def get_stats():
    stats = {}

    cpu_load = [x / os.cpu_count() * 100 for x in os.getloadavg()][1]
    stats['cpu_load'] = round(cpu_load)

    return stats

if __name__ == "__main__":
    stats = get_stats()
    print(stats)
