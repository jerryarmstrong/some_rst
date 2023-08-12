tests/ui/lint/rfc-2383-lint-reason/expect_missing_feature_gate.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // should error due to missing feature gate.

#![warn(unused)]

#[expect(unused)]
//~^ ERROR: the `#[expect]` attribute is an experimental feature [E0658]
fn main() {
    let x = 1;
}


