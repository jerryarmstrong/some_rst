tests/ui/check-cfg/allow-macro-cfg.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test check that local #[allow(unexpected_cfgs)] works
//
// check-pass
// compile-flags:--check-cfg=names() -Z unstable-options

#[allow(unexpected_cfgs)]
fn foo() {
    if cfg!(FALSE) {}
}

fn main() {
    #[allow(unexpected_cfgs)]
    if cfg!(FALSE) {}
}


