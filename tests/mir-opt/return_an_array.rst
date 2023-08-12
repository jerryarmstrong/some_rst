tests/mir-opt/return_an_array.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // this tests move up progration, which is not yet implemented

fn foo() -> [u8; 1024] {
        let x = [0; 1024];
        return x;
}

fn main() { }


