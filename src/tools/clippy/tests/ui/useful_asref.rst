src/tools/clippy/tests/ui/useful_asref.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::useless_asref)]

trait Trait {
    fn as_ptr(&self);
}

impl<'a> Trait for &'a [u8] {
    fn as_ptr(&self) {
        self.as_ref().as_ptr();
    }
}

fn main() {}


