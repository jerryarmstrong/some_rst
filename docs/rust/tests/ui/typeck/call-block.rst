tests/ui/typeck/call-block.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = {42}(); //~ ERROR expected function, found `{integer}`
}


