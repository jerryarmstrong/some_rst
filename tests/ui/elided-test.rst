tests/ui/elided-test.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: `main` function not found

// Since we're not compiling a test runner this function should be elided
// and the build will fail because main doesn't exist
#[test]
fn main() {
}


