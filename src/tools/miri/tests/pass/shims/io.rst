src/tools/miri/tests/pass/shims/io.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(is_terminal)]

use std::io::IsTerminal;

fn main() {
    // We can't really assume that this is truly a terminal, and anyway on Windows Miri will always
    // return `false` here, but we can check that the call succeeds.
    std::io::stdout().is_terminal();
}


