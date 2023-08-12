tests/ui/index_message.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let z = ();
    let _ = z[0]; //~ ERROR cannot index into a value of type `()`
}


