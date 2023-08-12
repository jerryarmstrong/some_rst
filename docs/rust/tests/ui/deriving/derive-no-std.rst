tests/ui/deriving/derive-no-std.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:derive-no-std.rs

extern crate derive_no_std;
use derive_no_std::*;

fn main() {
    let f = Foo { x: 0 };
    assert_eq!(f.clone(), Foo::default());

    assert!(Bar::Qux < Bar::Quux(42));
}


