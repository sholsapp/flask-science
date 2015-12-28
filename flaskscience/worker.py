import logging
import random
import threading
import time


log = logging.getLogger(__name__)


#: A function that takes no arguments and does nothing.
no_op = lambda: time.time()


class DataCollector(threading.Thread):
  """A background worker.

  :param dict database: A database in which to store data. The database must
    be dict-like and support indexing.
  :param int interval: The number of seconds to wait before re-running the work
    function.

  """

  def __init__(self, database, interval=60):
    threading.Thread.__init__(self)
    self.database = database
    self.interval = interval
    self.running = True

  def stop(self):
    """Stop the execution thread."""
    self.running = False

  def run(self):
    """Start the execution thread."""
    while self.running:
      if not self.collect():
        log.warning('Collection method returned invalid response!')
      time.sleep(self.interval)

  def collect(self):
    """Collect data.

    This method should be overridden by a specialized collector. See
    :class:`RandomDataCollector` for an example.

    """
    raise NotImplementedError


class RandomDataCollector(DataCollector):
  """Collect random time series data.

  This class specializes only the `collect` method to do random work and is
  intended to be used as an example of inheritance only.

  """

  def collect(self):
    now = int(time.time())
    rand = random.randint(0, 100)
    log.debug('Collecting data: (%s, %s)', now, rand)
    self.database[int(time.time())] = random.randint(0, 100)
    return True
