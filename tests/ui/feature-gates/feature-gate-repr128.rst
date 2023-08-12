tests/ui/feature-gates/feature-gate-repr128.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(u128)]
enum A { //~ ERROR repr with 128-bit type is unstable
    A(u64)
}

fn main() {}


