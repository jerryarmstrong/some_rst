tests/ui/consts/const-byte-str-cast.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#[deny(warnings)]

pub fn main() {
    let _ = b"x" as &[u8];
    let _ = b"y" as &[u8; 1];
    let _ = b"z" as *const u8;
    let _ = "ä" as *const str;
}


