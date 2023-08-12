tests/ui/issues/issue-4333.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
// pretty-expanded FIXME #23616

use std::io;

pub fn main() {
    let stdout = &mut io::stdout() as &mut dyn io::Write;
    stdout.write(b"Hello!");
}


