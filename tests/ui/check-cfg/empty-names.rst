tests/ui/check-cfg/empty-names.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check warning for unexpected cfg
//
// check-pass
// compile-flags: --check-cfg=names() -Z unstable-options

#[cfg(unknown_key = "value")]
//~^ WARNING unexpected `cfg` condition name
pub fn f() {}

fn main() {}


