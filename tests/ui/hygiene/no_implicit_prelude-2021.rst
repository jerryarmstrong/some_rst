tests/ui/hygiene/no_implicit_prelude-2021.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2021

#![no_implicit_prelude]

fn main() {
    assert!(true, "hoi");
    assert!(false, "hoi {}", 123);
}


