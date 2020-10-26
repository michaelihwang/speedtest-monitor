import sys
import time
from datetime import datetime
from traceback import print_exc

import speedtest

from decorator import restartable

KILOBYTE = 1024
MEGABYTE = 1024 * KILOBYTE
REPORT_FREQ = 60

def test_setup(st):
    st.get_servers()
    st.get_best_server()
    st.download()   # bits/s
    st.upload()     # bits/s

    res = st.results.dict()
    download = "{:.2f}".format(res["download"] / MEGABYTE)
    upload = "{:.2f}".format(res["upload"] / MEGABYTE)
    ping = "{:.2f}".format(res["ping"])
    return download, upload, ping


@restartable
def main():
    # Check if command line argument for reporting freq is provided (min 30)
    if len(sys.argv) and int(sys.argv[1]) >= 30:
        REPORT_FREQ = int(sys.argv[1])

    try:
        st = speedtest.Speedtest()
        while True:
            time_now = datetime.now().strftime("%H:%M:%S")
            download, upload, ping = test_setup(st)
            print(f"[{time_now}]: PING: {ping} ms\tDOWN: {download} Mbps\tUP: {upload} Mbps")
            time.sleep(REPORT_FREQ)
    except Exception as exc:
        print("\nCaught exception: ", exc.__class__.__name__)
        print_exc()


if __name__ == "__main__":
    main()

