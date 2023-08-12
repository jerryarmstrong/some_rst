tests/ui/lint/lint-renamed.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[deny(bare_trait_object)]
//~^ WARN lint `bare_trait_object` has been renamed to `bare_trait_objects`
#[deny(unused)]
fn main() { let unused = (); } //~ ERROR unused


