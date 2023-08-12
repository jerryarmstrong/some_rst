tests/ui/feature-gates/feature-gate-no_sanitize.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_sanitize(address)]
//~^ the `#[no_sanitize]` attribute is an experimental feature
fn main() {
}


