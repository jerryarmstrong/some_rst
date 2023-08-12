tests/ui/rust-2021/prelude2021.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2021

fn main() {
    let _: u16 = 123i32.try_into().unwrap();
}


