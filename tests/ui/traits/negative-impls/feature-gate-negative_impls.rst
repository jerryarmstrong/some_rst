tests/ui/traits/negative-impls/feature-gate-negative_impls.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait MyTrait {}
impl !MyTrait for u32 {} //~ ERROR negative trait bounds are not yet fully implemented
fn main() {}


