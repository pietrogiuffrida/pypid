#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pypid import PyPid

if __name__ == '__main__':

    p = PyPid('pid_filename.pid')
    p.open()
    p.close()