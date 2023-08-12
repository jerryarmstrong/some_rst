tests/ui/macros/recovery-allowed.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! please_recover {
    ($a:expr) => {};
}

please_recover! { not 1 }
//~^ ERROR unexpected `1` after identifier

fn main() {}


