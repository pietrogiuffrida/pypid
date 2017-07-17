#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import psutil


def writeLockfile(lockfilepath):
  pid = os.getpid()
  process = psutil.Process(pid)
  pname = process.cmdline()[1]

  lockfile = open(lockfilepath, 'w')
  lockfile.write(str(pid))
  lockfile.close()


def checkpid(lockfilepath):
  exist_status = 0

  if os.path.exists(lockfilepath):
    exist_status = 1
    logging.error('ESISTE UN FILE DI LOCK PRECEDENTE!')

    pid = open(lockfilepath, 'r').read()

    if not pid.isdigit():
      exist_status = 2
      logging.error('IL PID È MALFORMATO')

    if psutil.pid_exists(int(pid)):
      exist_status = 3
      logging.error('IL PROCESSO {} È ANCORA IN ESECUZIONE!!!'.format(pid))

  return exist_status


def deleteLockfile(lockfilepath):
  os.remove(lockfilepath)


