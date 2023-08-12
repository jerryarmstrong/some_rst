src/tools/miri/tests/fail/unsupported_foreign_function.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@normalize-stderr-test: "OS `.*`" -> "$$OS"

fn main() {
    extern "Rust" {
        fn foo();
    }

    unsafe {
        foo(); //~ ERROR: unsupported operation: can't call foreign function `foo`
    }
}


