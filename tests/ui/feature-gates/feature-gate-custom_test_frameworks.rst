tests/ui/feature-gates/feature-gate-custom_test_frameworks.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![test_runner(main)] //~ ERROR custom test frameworks are an unstable feature

#[test_case] //~ ERROR custom test frameworks are an unstable feature
fn f() {}

fn main() {}


