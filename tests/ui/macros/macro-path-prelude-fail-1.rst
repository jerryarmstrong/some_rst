tests/ui/macros/macro-path-prelude-fail-1.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod m {
    fn check() {
        Vec::clone!(); //~ ERROR failed to resolve: `Vec` is a struct, not a module
        u8::clone!(); //~ ERROR failed to resolve: `u8` is a builtin type, not a module
    }
}

fn main() {}


