tests/ui/methods/method-call-type-binding.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    0.clone::<T = u8>(); //~ ERROR associated type bindings are not allowed here
}


