src/compiler-rt/unittests/lit.common.unit.cfg.py
================================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: py

    # -*- Python -*-

# Configuration file for 'lit' test runner.
# This file contains common config setup rules for unit tests in various
# compiler-rt testsuites.

import os

import lit.formats

# Setup test format
llvm_build_mode = getattr(config, "llvm_build_mode", "Debug")
config.test_format = lit.formats.GoogleTest(llvm_build_mode, "Test")

# Setup test suffixes.
config.suffixes = []

# Tweak PATH to include llvm tools dir.
llvm_tools_dir = config.llvm_tools_dir
if (not llvm_tools_dir) or (not os.path.exists(llvm_tools_dir)):
  lit_config.fatal("Invalid llvm_tools_dir config attribute: %r" % llvm_tools_dir)
path = os.path.pathsep.join((llvm_tools_dir, config.environment['PATH']))
config.environment['PATH'] = path

# Propagate the temp directory. Windows requires this because it uses \Windows\
# if none of these are present.
if 'TMP' in os.environ:
    config.environment['TMP'] = os.environ['TMP']
if 'TEMP' in os.environ:
    config.environment['TEMP'] = os.environ['TEMP']

if config.host_os == 'Darwin':
  # Only run up to 3 processes that require shadow memory simultaneously on
  # 64-bit Darwin. Using more scales badly and hogs the system due to
  # inefficient handling of large mmap'd regions (terabytes) by the kernel.
  lit_config.parallelism_groups["shadow-memory"] = 3

  # The test config gets pickled and sent to multiprocessing workers, and that
  # only works for code if it is stored at the top level of some module.
  # Therefore, we have to put the code in a .py file, add it to path, and import
  # it to store it in the config.
  import site
  site.addsitedir(os.path.dirname(__file__))
  import lit_unittest_cfg_utils
  config.darwin_sanitizer_parallelism_group_func = \
    lit_unittest_cfg_utils.darwin_sanitizer_parallelism_group_func


