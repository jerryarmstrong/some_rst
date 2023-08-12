tests/ui/svh/auxiliary/changing-crates-b.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "b"]

extern crate a;

pub fn foo() { a::foo::<isize>(); }


