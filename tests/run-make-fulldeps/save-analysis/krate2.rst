tests/run-make-fulldeps/save-analysis/krate2.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![ crate_name = "krate2" ]
#![ crate_type = "lib" ]

use std::io::Write;

pub fn hello() {
    std::io::stdout().write_all(b"hello world!\n");
}


