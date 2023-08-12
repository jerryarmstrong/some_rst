tests/ui/issues/issue-4542.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use std::env;

pub fn main() {
    for arg in env::args() {
        match arg.clone() {
            _s => { }
        }
    }
}


