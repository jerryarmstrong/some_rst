tests/ui/lint/lint-forbid-attr.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![forbid(deprecated)]

#[allow(deprecated)]
//~^ ERROR allow(deprecated) incompatible
//~| ERROR allow(deprecated) incompatible
fn main() {
}


