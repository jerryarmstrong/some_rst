tests/ui/rust-2018/edition-lint-fully-qualified-paths.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![feature(rust_2018_preview)]
#![deny(absolute_paths_not_starting_with_crate)]

mod foo {
    pub(crate) trait Foo {
        type Bar;
    }

    pub(crate) struct Baz {}

    impl Foo for Baz {
        type Bar = ();
    }
}

fn main() {
    let _: <foo::Baz as ::foo::Foo>::Bar = ();
    //~^ ERROR absolute paths must start with
    //~| this is accepted in the current edition

    let _: <::foo::Baz as foo::Foo>::Bar = ();
    //~^ ERROR absolute paths must start with
    //~| this is accepted in the current edition
}


