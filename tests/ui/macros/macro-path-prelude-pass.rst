tests/ui/macros/macro-path-prelude-pass.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

mod m {
    fn check() {
        std::panic!(); // OK
    }
}

fn main() {}


