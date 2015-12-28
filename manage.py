#!/usr/bin/env python

import logging

from flask.ext.script import Manager

from flaskscience import app, database
from flaskscience.worker import RandomDataCollector


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


manager = Manager(app)


@manager.command
def runserver(*args, **kwargs):
  """Override default `runserver` to init webapp before running."""
  worker = RandomDataCollector(database, interval=1)
  worker.start()
  app.run(*args, **kwargs)
  while worker.is_alive():
    try:
      worker.join(1)
    except KeyboardInterrupt:
      log.info('Shutting down worker thread!')
      worker.stop()


if __name__ == "__main__":
  manager.run()
