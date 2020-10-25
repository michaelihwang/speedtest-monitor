# Python Internet Speed Monitor
Monitor your internet download and upload speed via the Command Line with this Python Script!

By default, the script reports every 60 seconds / 1 minute. To change its frequency, simply provide int argument when running the script:
i.e. `python3 script.py 300` to report download and upload speed every 5 minutes (60 * 5 = 300).

Note: Min reporting frequency is set to 30 seconds.

## Setup and Running Script

1. Clone this repository via `git clone https://github.com/michaelihwang/speedtest-monitor.git`.

2. Use `pip3 install -r requirements.txt` to install dependencies if they are missing.

3. On the command line, run `$ python3 script.py` for default 1 minute reports, or with an argument like the example above.

4. To quit, `cntrl + c`.

## License
MIT License Copyright © 2020 Michael Hwang
