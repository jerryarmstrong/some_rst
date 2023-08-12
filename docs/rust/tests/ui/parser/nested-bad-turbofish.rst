tests/ui/parser/nested-bad-turbofish.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    foo<<S as T>::V>(); //~ ERROR
}


