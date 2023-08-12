tests/ui/issues/issue-2063-resource.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
// test that autoderef of a type like this does not
// cause compiler to loop.  Note that no instances
// of such a type could ever be constructed.

struct S {
  x: X,
  to_str: (),
}

struct X(Box<S>);

fn main() {}


