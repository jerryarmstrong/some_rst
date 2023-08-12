src/tools/clippy/tests/ui/bytes_nth.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(clippy::unnecessary_operation)]
#![warn(clippy::bytes_nth)]

fn main() {
    let s = String::from("String");
    let _ = s.bytes().nth(3);
    let _ = &s.bytes().nth(3);
    let _ = s[..].bytes().nth(3);
}


