tests/ui/rfcs/rfc-1937-termination-trait/termination-trait-for-impl-termination.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() -> impl std::process::Termination { }


