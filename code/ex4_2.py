import re
import datetime


def extract_info(text):
    info_date = re.findall("\[(.*)\]", text)[0]
    # convert to datetime format
    fmt = '%Y-%m-%d %H:%M'
    info_date = datetime.datetime.strptime(info_date, fmt)
    info_action = re.findall("\] (.*)", text)[0]
    return [info_date, info_action]


def extract_more(text):

    if "Guard" in text[1]:
        guard_id = re.findall("#([0-9]{1,})", text[1])[0]
        global guard_cache
        guard_cache = guard_id
        if guard_id in per_guard.keys():
            pass
        else:
            per_guard[guard_id] = []

    elif "falls" in text[1]:
        per_guard[guard_cache].append(text[0])

    elif "wakes" in text[1]:
        per_guard[guard_cache].append(text[0])


def get_time_asleep(key, items):
    per_gurad_time_asleep[key] = sum([(items[i + 1] - items[i]).total_seconds() / 60 for i in range(0, len(items), 2)])


def get_critical_time(key, items):
    temp = [0 for i in range(60)]
    for e in range(0, len(items), 2):
        for x in range(items[e].minute, items[e + 1].minute):
            temp[x] = temp[x] + 1

    max_time = temp.index(max(temp))
    per_guar_critical[key] = [max_time, max(temp)]


lines = open("../data/day4.txt").read().split("\n")[:-1]
# 2 informations per observation: date, action
extracted = [extract_info(line) for line in lines]
# sort by asecending dateprint(key(extracted[0]))
extracted.sort(key=lambda r: r[0])
# create dictionary of guards with time_sleep, time_wakeup
per_guard = {}
[extract_more(e) for e in extracted]
per_guar_critical = {}
[get_critical_time(key, items) for key, items in per_guard.items()]
max_intersect = max([items[1] for key, items in per_guar_critical.items()])
that_gurad_time = [(int(key), int(items[0])) for key, items in per_guar_critical.items() if items[1] == max_intersect][0]
print(that_gurad_time[0] * that_gurad_time[1])
