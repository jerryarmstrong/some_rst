tests/ui/feature-gates/feature-gate-public_private_dependencies.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test is different from other feature gate tests.
// Instead of checking that an error occurs without the feature gate,
// it checks that *no* errors/warnings occurs without the feature gate.
// This is due to the fact that 'public_private_dependencies' just enables
// a lint, so disabling it shouldn't cause any code to stop compiling.

// run-pass
// aux-build:pub_dep.rs

// Without ![feature(public_private_dependencies)],
// this should do nothing/
#![deny(exported_private_dependencies)]

extern crate pub_dep;

pub struct Foo {
    pub field: pub_dep::PubType
}

fn main() {}


