tests/ui/const-generics/defaults/default-param-wf-concrete.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<const N: u8 = { 255 + 1 }>;
//~^ ERROR evaluation of constant value failed
fn main() {}


