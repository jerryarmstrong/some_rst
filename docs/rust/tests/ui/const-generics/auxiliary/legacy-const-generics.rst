tests/ui/const-generics/auxiliary/legacy-const-generics.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_legacy_const_generics(1)]
pub fn foo<const Y: usize>(x: usize, z: usize) -> [usize; 3] {
    [x, Y, z]
}


