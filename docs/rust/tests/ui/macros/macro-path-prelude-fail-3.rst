tests/ui/macros/macro-path-prelude-fail-3.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    inline!(); //~ ERROR cannot find macro `inline` in this scope
}


