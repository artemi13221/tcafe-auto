import os
import schedule
import datetime
import logging
import random
import time


def get_now():
    return ("[" + str(datetime.datetime.now()) + "]")


def run_tcafe():
    try:
        os.system("python3 tcafe.py")
        logging.info(get_now() + '- Success launched tcafe.py')
    except:
        logging.error(get_now() + '- Failed launched tcafe.py')


if __name__ == '__main__':
    logging.basicConfig(filename='tcafe.log',
                        encoding='utf-8', level=logging.DEBUG)
    logging.info(get_now() + '- Started automatic attending tcafe')
    schedule.every().day.at("10:" + str(random.randint(0, 59)))

    while True:
        schedule.run_pending()
        time.sleep(5)
