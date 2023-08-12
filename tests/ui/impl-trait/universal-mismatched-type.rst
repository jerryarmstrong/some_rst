tests/ui/impl-trait/universal-mismatched-type.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;

fn foo(x: impl Debug) -> String {
    x //~ ERROR mismatched types
}

fn main() { }


