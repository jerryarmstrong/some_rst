tests/ui/const-generics/type_not_in_scope.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl X {
    //~^ ERROR cannot find type
    fn getn<const N: usize>() -> [u8; N] {
        getn::<N>()
    }
}
fn getn<const N: cfg_attr>() -> [u8; N] {}
//~^ ERROR expected type, found built-in attribute `cfg_attr`
//~| ERROR mismatched types

fn main() {}


