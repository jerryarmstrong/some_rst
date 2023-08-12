tests/ui/check-cfg/allow-upper-level.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test check that #[allow(unexpected_cfgs)] work if put on an upper level
//
// check-pass
// compile-flags:--check-cfg=names() -Z unstable-options

#[allow(unexpected_cfgs)]
mod aa {
    #[cfg(FALSE)]
    fn bar() {}
}

fn main() {}


