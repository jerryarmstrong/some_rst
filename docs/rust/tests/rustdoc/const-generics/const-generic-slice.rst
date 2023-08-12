tests/rustdoc/const-generics/const-generic-slice.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

pub trait Array {
    type Item;
}

// @has foo/trait.Array.html
// @has - '//*[@class="impl has-srclink"]' 'impl<T, const N: usize> Array for [T; N]'
impl<T, const N: usize> Array for [T; N] {
    type Item = T;
}


