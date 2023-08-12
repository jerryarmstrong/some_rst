src/tools/miri/tests/fail/rustc-error.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure we exit with non-0 status code when the program fails to build.
fn main() {
    println("Hello, world!"); //~ ERROR: expected function, found macro
}


