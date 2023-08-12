tests/ui/keyword/keyword-self-as-identifier.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let Self = 22; //~ ERROR cannot find unit struct, unit variant or constant `Self` in this scope
}


