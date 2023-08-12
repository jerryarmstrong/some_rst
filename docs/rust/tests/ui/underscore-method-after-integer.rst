tests/ui/underscore-method-after-integer.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Tr : Sized {
    fn _method_on_numbers(self) {}
}

impl Tr for i32 {}

fn main() {
    42._method_on_numbers();
}


