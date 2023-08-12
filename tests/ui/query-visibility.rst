tests/ui/query-visibility.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Check that it doesn't panic when `Input` gets its visibility checked.

#![crate_type = "lib"]

pub trait Layer<
    /// Hello.
    Input,
> {}


