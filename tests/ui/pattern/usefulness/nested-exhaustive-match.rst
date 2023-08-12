tests/ui/pattern/usefulness/nested-exhaustive-match.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

struct Foo { foo: bool, bar: Option<isize>, baz: isize }

pub fn main() {
    match (Foo{foo: true, bar: Some(10), baz: 20}) {
      Foo{foo: true, bar: Some(_), ..} => {}
      Foo{foo: false, bar: None, ..} => {}
      Foo{foo: true, bar: None, ..} => {}
      Foo{foo: false, bar: Some(_), ..} => {}
    }
}


