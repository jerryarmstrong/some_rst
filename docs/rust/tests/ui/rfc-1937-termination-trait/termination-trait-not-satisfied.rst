tests/ui/rfc-1937-termination-trait/termination-trait-not-satisfied.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct ReturnType {}

fn main() -> ReturnType { //~ ERROR `main` has invalid return type `ReturnType`
    ReturnType {}
}


