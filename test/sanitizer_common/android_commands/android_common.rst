test/sanitizer_common/android_commands/android_common.py
========================================================

Last edited: 2018-11-24 20:57:03

Contents:

.. code-block:: py

    import os, sys, subprocess, tempfile
import time

ANDROID_TMPDIR = '/data/local/tmp/Output'
ADB = os.environ.get('ADB', 'adb')

verbose = False
if os.environ.get('ANDROID_RUN_VERBOSE') == '1':
    verbose = True

def host_to_device_path(path):
    rel = os.path.relpath(path, "/")
    dev = os.path.join(ANDROID_TMPDIR, rel)
    return dev

def adb(args, attempts = 1):
    if verbose:
        print args
    tmpname = tempfile.mktemp()
    out = open(tmpname, 'w')
    ret = 255
    while attempts > 0 and ret != 0:
      attempts -= 1
      ret = subprocess.call([ADB] + args, stdout=out, stderr=subprocess.STDOUT)
      if attempts != 0:
        ret = 5
    if ret != 0:
      print "adb command failed", args
      print tmpname
      out.close()
      out = open(tmpname, 'r')
      print out.read()
    out.close()
    os.unlink(tmpname)
    return ret

def pull_from_device(path):
    tmp = tempfile.mktemp()
    adb(['pull', path, tmp], 5)
    text = open(tmp, 'r').read()
    os.unlink(tmp)
    return text

def push_to_device(path):
    dst_path = host_to_device_path(path)
    adb(['push', path, dst_path], 5)


