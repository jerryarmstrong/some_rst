tests/ui/const-generics/defaults/auxiliary/trait_object_lt_defaults_lib.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo<'a, const N: usize, T: 'a + ?Sized>(pub &'a T, [(); N]);


