tests/ui/extern/extern-main-issue-86110.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // missing and missing2 exist to make sure that the error only happens on a `main` declaration
extern "C" {
    fn missing();
    fn main();
    //~^ the `main` function cannot be declared in an `extern` block
    fn missing2();
}


