tools/llvm-shlib/gen-msvc-exports.py
====================================

Last edited: 2020-02-10 23:18:46

Contents:

.. code-block:: py

    #===- gen-msvc-exports.py - Generate C API export file -------*- python -*--===#
#
#                     The LLVM Compiler Infrastructure
#
# This file is distributed under the University of Illinois Open Source
# License. See LICENSE.TXT for details.
#
#===------------------------------------------------------------------------===#
#
# Generate an export file from a list of given LIB files. This only exports symbols
# that start with LLVM, so it only exports the LLVM C API.
#
# To have CMake run this, set LLVM_BUILD_LLVM_C_DYLIB to on while
# building on Windows.
#
# To run manually, build LLVM with Visual Studio, use a Command prompt
# to navigate to the directory with the .lib files (Debug\lib etc). Then run
#     python C:\Path\To\gen-msvc-exports.py --nm ..\bin\llvm-nm.exe LLVM*.lib
#
# If you're generating a 32 bit DLL, use the `--underscore` flag.
# If you want to use a different `llvm-nm` executable, pass the path
# with the `--nm` flag.
#
# You can use the --output flag to set the name of the export file.
#
#===------------------------------------------------------------------------===#
from tempfile import mkstemp
from contextlib import contextmanager
from subprocess import check_call
import argparse
import os
import re


_UNDERSCORE_REGEX = {
    False: re.compile(r"^\w+\s+T\s+(LLVM.*)$"),
    True:  re.compile(r"^\w+\s+T\s+_(LLVM.*)$")
}


@contextmanager
def removing(path):
    try:
        yield path
    finally:
        os.unlink(path)


def touch_tempfile(*args, **kwargs):
    fd, name = mkstemp(*args, **kwargs)
    os.close(fd)
    return name


def gen_llvm_c_export(output, underscore, libs, nm):
    """Generate the export file for the LLVM-C DLL.

    Run `nm` for each lib in `libs`, and output an export file
    to `output`. If `underscore` is true, symbols will
    be assumed to be prefixed with an underscore.
    """
    with removing(touch_tempfile(prefix='dumpout', suffix='.txt')) as dumpout:

        # Get the right regex.
        p = _UNDERSCORE_REGEX[underscore]

        with open(output, 'w+t') as output_f:

            # For each lib get the LLVM* functions it exports.
            for lib in libs:
                # Call dumpbin.
                with open(dumpout, 'w+t') as dumpout_f:
                    check_call([nm, '-g', lib], stdout=dumpout_f)

                # Get the matching lines.
                with open(dumpout) as dumpbin:
                    for line in dumpbin:
                        m = p.match(line)
                        if m is not None:
                            output_f.write(m.group(1) + '\n')


def main():
    parser = argparse.ArgumentParser('gen-msvc-exports')

    parser.add_argument(
        '-o', '--output', help='output filename', default='LLVM-C.exports'
    )
    parser.add_argument('-u', '--underscore',
        help='labels are prefixed with an underscore (use for 32 bit DLLs)',
        action='store_true'
    )
    parser.add_argument(
        '--nm', help='path to the llvm-nm executable', default='llvm-nm'
    )
    parser.add_argument(
        'libs', metavar='LIBS', nargs='+', help='list of libraries to generate export from'
    )

    ns = parser.parse_args()

    gen_llvm_c_export(ns.output, ns.underscore, ns.libs, ns.nm)


if __name__ == '__main__':
    main()


