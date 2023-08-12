tests/ui/resolve/resolve-self-in-impl-2.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S<T = u8>(T);
trait Tr<T = u8> {}

impl Self for S {} //~ ERROR expected trait, found self type `Self`
impl Self::N for S {} //~ ERROR cannot find trait `N` in `Self`

fn main() {}


