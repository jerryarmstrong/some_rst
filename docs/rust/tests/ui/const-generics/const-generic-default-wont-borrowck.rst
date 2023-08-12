tests/ui/const-generics/const-generic-default-wont-borrowck.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct X<const N: usize = {
    let s: &'static str; s.len() //~ ERROR E0381
}>;

fn main() {}


