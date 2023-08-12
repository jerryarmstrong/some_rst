tests/ui/consts/const-err-rpass.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// check for const_err regressions

const X: *const u8 = b"" as _;
const Y: bool = 'A' == 'B';
const Z: char = 'A';
const W: bool = Z <= 'B';


fn main() {
    let _ = ((-1 as i8) << 8 - 1) as f32;
    let _ = 0u8 as char;
    let _ = true > false;
    let _ = true >= false;
    let _ = true < false;
    let _ = true >= false;
}


