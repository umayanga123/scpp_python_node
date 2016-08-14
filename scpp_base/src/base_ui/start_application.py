import logging
import time

import stock_exchange


def calc(connector, progress):
  progress.set(0, 10)
  for i in range(10, 0, -1):
    progress.tick()
    connector.ack()  # can be ommitted in this program
    time.sleep(.2)

  stock_exchange.init()
  stock_exchange.log()
  stock_exchange.main()




