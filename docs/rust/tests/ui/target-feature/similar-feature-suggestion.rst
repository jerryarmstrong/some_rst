tests/ui/target-feature/similar-feature-suggestion.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Ctarget-feature=+rdrnd --crate-type=rlib --target=x86_64-unknown-linux-gnu
// build-pass
// needs-llvm-components: x86

#![feature(no_core)]
#![no_core]


