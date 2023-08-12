tests/ui/return/return-unit-from-diverging.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we get the usual error that we'd get for any other return type and not something about
// diverging functions not being able to return.

fn fail() -> ! {
    return; //~ ERROR in a function whose return type is not
}

fn main() {
}


