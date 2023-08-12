tests/ui/check-cfg/allow-same-level.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test check that #[allow(unexpected_cfgs)] doesn't work if put on the same level
//
// check-pass
// compile-flags:--check-cfg=names() -Z unstable-options

#[allow(unexpected_cfgs)]
#[cfg(FALSE)]
//~^ WARNING unexpected `cfg` condition name
fn bar() {}

fn main() {}


