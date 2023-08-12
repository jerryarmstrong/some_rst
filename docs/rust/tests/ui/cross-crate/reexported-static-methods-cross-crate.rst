tests/ui/cross-crate/reexported-static-methods-cross-crate.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:reexported_static_methods.rs

extern crate reexported_static_methods;

use reexported_static_methods::Foo;
use reexported_static_methods::Baz;
use reexported_static_methods::Boz;
use reexported_static_methods::Bort;

pub fn main() {
    assert_eq!(42_isize, Foo::foo());
    assert_eq!(84_isize, Baz::bar());
    assert!(Boz::boz(1));
    assert_eq!("bort()".to_string(), Bort::bort());
}


