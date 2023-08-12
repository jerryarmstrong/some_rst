tests/ui/feature-gates/feature-gate-auto-traits.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that default and negative trait implementations are gated by
// `auto_traits` feature gate

struct DummyStruct;

auto trait AutoDummyTrait {}
//~^ ERROR auto traits are experimental and possibly buggy

impl !AutoDummyTrait for DummyStruct {}
//~^ ERROR negative trait bounds are not yet fully implemented; use marker types for now

fn main() {}


