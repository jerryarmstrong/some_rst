tests/ui/consts/const-block-non-item-statement-3.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code, unused)]

type Array = [u32; {  let x = 2; 5 }];

pub fn main() {
    let _: Array = [0; 5];
}


