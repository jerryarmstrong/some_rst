tests/ui/macros/issue-78325-inconsistent-resolution.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! define_other_core {
    ( ) => {
        extern crate std as core;
        //~^ ERROR macro-expanded `extern crate` items cannot shadow names passed with `--extern`
    };
}

fn main() {
    core::panic!();
}

define_other_core!();


