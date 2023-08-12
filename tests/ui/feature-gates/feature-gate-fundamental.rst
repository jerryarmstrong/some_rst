tests/ui/feature-gates/feature-gate-fundamental.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[fundamental] //~ ERROR the `#[fundamental]` attribute is an experimental feature
struct Fundamental;

fn main() { }


