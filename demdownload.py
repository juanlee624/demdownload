# -*- coding: utf-8 -*-


from gevent import monkey

monkey.patch_all()
from gevent.pool import Pool
import requests
import sys
import os


def download(url):
    chrome = 'Mozilla/5.0 (X11; Linux i86_64) AppleWebKit/537.36 ' + '(KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    headers = {'User-Agent': chrome}
    # filename = url.split('/')[-1].strip()
    filename = "respose.log"
    r = requests.get(url.strip(), headers=headers, stream=True)
    with open(filename, 'a+') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
        f.flush()
        print
        filename, "is ok"


def removeLine(key, filename):
    os.system('sed -i /%s/d %s' % (key, filename))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        f = open(filename, "r")
        p = Pool(4)
        for line in f.readlines():
            if line:
                p.spawn(download, line.strip())
                key = line.split('/')[-1].strip()
                # removeLine(key, filename)
                f.close()
                p.join()
    else:
        print
        'Usage: python %s urls.txt' % sys.argv[0]

