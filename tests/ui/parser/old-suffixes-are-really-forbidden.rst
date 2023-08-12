tests/ui/parser/old-suffixes-are-really-forbidden.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a = 1_is; //~ ERROR invalid suffix
    let b = 2_us; //~ ERROR invalid suffix
}


