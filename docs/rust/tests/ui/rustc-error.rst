tests/ui/rustc-error.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_error]
fn main() {
    //~^ ERROR fatal error triggered by #[rustc_error]
}


