src/tools/miri/tests/panic/unsupported_foreign_function.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-panic-on-unsupported
//@normalize-stderr-test: "OS `.*`" -> "$$OS"

fn main() {
    extern "Rust" {
        fn foo();
    }

    unsafe {
        foo();
    }
}


