tests/ui/privacy/pub-use-xcrate.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:pub_use_xcrate1.rs
// aux-build:pub_use_xcrate2.rs

// pretty-expanded FIXME #23616

extern crate pub_use_xcrate2;

use pub_use_xcrate2::Foo;

pub fn main() {
    let _foo: Foo = Foo {
        name: 0
    };
}


