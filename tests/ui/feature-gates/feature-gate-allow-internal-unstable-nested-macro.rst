tests/ui/feature-gates/feature-gate-allow-internal-unstable-nested-macro.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-allow_internal_unstable

#![allow(unused_macros)]

macro_rules! bar {
    () => {
        // more layers don't help:
        #[allow_internal_unstable()] //~ ERROR allow_internal_unstable side-steps
        macro_rules! baz {
            () => {}
        }
    }
}

bar!();

fn main() {}


