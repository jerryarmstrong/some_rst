tests/ui/using-target-feature-unstable.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// only-x86_64
// aux-build:using-target-feature-unstable.rs

extern crate using_target_feature_unstable;

fn main() {
    unsafe {
        using_target_feature_unstable::foo();
    }
}


