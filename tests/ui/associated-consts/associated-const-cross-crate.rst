tests/ui/associated-consts/associated-const-cross-crate.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:associated-const-cc-lib.rs


extern crate associated_const_cc_lib as foolib;

pub struct LocalFoo;

impl foolib::Foo for LocalFoo {
    const BAR: usize = 1;
}

fn main() {
    assert_eq!(0, <foolib::FooNoDefault as foolib::Foo>::BAR);
    assert_eq!(1, <LocalFoo as foolib::Foo>::BAR);
    assert_eq!(3, foolib::InherentBar::BAR);
}


