tests/rustdoc-ui/check-cfg.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: --check-cfg=names() -Z unstable-options

/// uniz is nor a builtin nor pass as arguments so is unexpected
#[cfg(uniz)]
//~^ WARNING unexpected `cfg` condition name
pub struct Bar;


