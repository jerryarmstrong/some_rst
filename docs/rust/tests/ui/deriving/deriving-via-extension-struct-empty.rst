tests/ui/deriving/deriving-via-extension-struct-empty.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#[derive(PartialEq, Debug)]
struct Foo;

pub fn main() {
  assert_eq!(Foo, Foo);
  assert!(!(Foo != Foo));
}


