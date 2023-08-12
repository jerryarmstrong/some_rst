tests/ui/deprecation/suggestion.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![feature(staged_api)]
#![feature(deprecated_suggestion)]

#![stable(since = "1.0.0", feature = "test")]

#![deny(deprecated)]
#![allow(dead_code)]

struct Foo;

impl Foo {
    #[deprecated(
        since = "1.0.0",
        note = "replaced by `replacement`",
        suggestion = "replacement",
    )]
    #[stable(since = "1.0.0", feature = "test")]
    fn deprecated(&self) {}

    fn replacement(&self) {}
}

mod bar {
    #[deprecated(
    since = "1.0.0",
    note = "replaced by `replacement`",
    suggestion = "replacement",
    )]
    #[stable(since = "1.0.0", feature = "test")]
    pub fn deprecated() {}

    pub fn replacement() {}
}

fn main() {
    let foo = Foo;

    foo.deprecated(); //~ ERROR use of deprecated

    bar::deprecated(); //~ ERROR use of deprecated
}


