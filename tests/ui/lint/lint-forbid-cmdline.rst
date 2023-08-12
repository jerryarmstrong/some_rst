tests/ui/lint/lint-forbid-cmdline.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -F deprecated

#[allow(deprecated)] //~ ERROR allow(deprecated) incompatible
                     //~| ERROR allow(deprecated) incompatible
fn main() {
}


