tests/ui/associated-consts/associated-const-cross-crate-defaults.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:associated-const-cc-lib.rs


extern crate associated_const_cc_lib as foolib;

pub struct LocalFooUseDefault;

impl foolib::FooDefault for LocalFooUseDefault {}

pub struct LocalFooOverwriteDefault;

impl foolib::FooDefault for LocalFooOverwriteDefault {
    const BAR: usize = 4;
}

fn main() {
    assert_eq!(1, <foolib::FooUseDefault as foolib::FooDefault>::BAR);
    assert_eq!(2, <foolib::FooOverwriteDefault as foolib::FooDefault>::BAR);
    assert_eq!(1, <LocalFooUseDefault as foolib::FooDefault>::BAR);
    assert_eq!(4, <LocalFooOverwriteDefault as foolib::FooDefault>::BAR);
}


