tests/ui/check-cfg/empty-values.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check warning for unexpected cfg value
//
// check-pass
// compile-flags: --check-cfg=values() -Z unstable-options

#[cfg(test = "value")]
//~^ WARNING unexpected `cfg` condition value
pub fn f() {}

fn main() {}


