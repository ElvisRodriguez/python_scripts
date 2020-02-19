
import sys
import time

def report_progress(ratio, width=50):
    filled = '=' * int(ratio * width)
    rest ='-' * (width - int(ratio*width))
    sys.stderr.write('\r|' + filled + rest + '|')
    sys.stderr.flush()

if __name__ == '__main__':
    for i in range(101):
        report_progress(i/100.0, 50)
        time.sleep(.01)
    print()
