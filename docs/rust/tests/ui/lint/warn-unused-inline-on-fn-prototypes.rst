tests/ui/lint/warn-unused-inline-on-fn-prototypes.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_attributes)]

trait Trait {
    #[inline] //~ ERROR `#[inline]` is ignored on function prototypes
    fn foo();
}

extern "C" {
    #[inline] //~ ERROR `#[inline]` is ignored on function prototypes
    fn foo();
}

fn main() {}


