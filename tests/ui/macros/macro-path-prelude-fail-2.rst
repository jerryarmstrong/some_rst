tests/ui/macros/macro-path-prelude-fail-2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod m {
    fn check() {
        Result::Ok!(); //~ ERROR failed to resolve: partially resolved path in a macro
    }
}

fn main() {}


