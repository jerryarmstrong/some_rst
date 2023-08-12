tests/ui/rust-2018/suggestions-not-always-applicable.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:suggestions-not-always-applicable.rs
// edition:2015
// run-rustfix
// rustfix-only-machine-applicable
// check-pass

#![feature(rust_2018_preview)]
#![warn(rust_2018_compatibility)]

extern crate suggestions_not_always_applicable as foo;

pub struct Foo;

mod test {
    use crate::foo::foo;

    #[foo]
    fn main() {}
}

fn main() {
    test::foo();
}


