tests/ui/structs-enums/namespaced-enums-xcrate.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:namespaced_enums.rs

// pretty-expanded FIXME #23616

extern crate namespaced_enums;

use namespaced_enums::Foo;

fn _foo (f: Foo) {
    match f {
        Foo::A | Foo::B(_) | Foo::C { .. } => {}
    }
}

pub fn main() {}


