tests/ui/consts/const-eval/dont_promote_unstable_const_fn_cross_crate.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:stability.rs

extern crate stability;

use stability::foo;

fn main() {
    let _: &'static u32 = &foo(); //~ ERROR temporary value dropped while borrowed
    let _x: &'static u32 = &foo(); //~ ERROR temporary value dropped while borrowed
}


