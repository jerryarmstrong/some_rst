tests/ui/const-generics/unused-const-param.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct A<const N: usize>; // ok

fn main() {}


