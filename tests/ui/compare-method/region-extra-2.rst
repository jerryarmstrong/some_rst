tests/ui/compare-method/region-extra-2.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #22779. An extra where clause was
// permitted on the impl that is not present on the trait.

trait Tr<'a, T> {
    fn renew<'b: 'a>(self) -> &'b mut [T];
}

impl<'a, T> Tr<'a, T> for &'a mut [T] {
    fn renew<'b: 'a>(self) -> &'b mut [T] where 'a: 'b {
        //~^ ERROR E0276
        &mut self[..]
    }
}

fn main() { }


