tests/ui/borrowck/borrowck-uninit-after-item.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let bar;
    fn baz(_x: isize) { }
    baz(bar); //~ ERROR E0381
}


