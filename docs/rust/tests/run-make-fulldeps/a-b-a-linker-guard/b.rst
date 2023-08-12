tests/run-make-fulldeps/a-b-a-linker-guard/b.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "b"]

extern crate a;

fn main() {
    a::foo(22_u32);
}


