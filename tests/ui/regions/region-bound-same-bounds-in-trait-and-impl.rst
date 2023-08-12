tests/ui/regions/region-bound-same-bounds-in-trait-and-impl.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test related to #22779, but where the `'a:'b` relation
// appears in the trait too. No error here.

// check-pass

trait Tr<'a, T> {
    fn renew<'b: 'a>(self) -> &'b mut [T] where 'a: 'b;
}

impl<'a, T> Tr<'a, T> for &'a mut [T] {
    fn renew<'b: 'a>(self) -> &'b mut [T] where 'a: 'b {
        &mut self[..]
    }
}


fn main() { }


