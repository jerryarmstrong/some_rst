tests/ui/feature-gates/feature-gate-start.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[start]
fn foo(_: isize, _: *const *const u8) -> isize { 0 }
//~^ ERROR `#[start]` functions are experimental


