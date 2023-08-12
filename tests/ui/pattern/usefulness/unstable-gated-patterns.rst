tests/ui/pattern/usefulness/unstable-gated-patterns.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unstable_test_feature)]

// aux-build:unstable.rs

extern crate unstable;

use unstable::UnstableEnum;

fn main() {
    match UnstableEnum::Stable {
        UnstableEnum::Stable => {}
        UnstableEnum::Stable2 => {}
    }
    //~^^^^ non-exhaustive patterns: `UnstableEnum::Unstable` not covered

    // Ok: all variants are explicitly matched
    match UnstableEnum::Stable {
        UnstableEnum::Stable => {}
        UnstableEnum::Stable2 => {}
        UnstableEnum::Unstable => {}
    }
}


