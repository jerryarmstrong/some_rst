tests/ui/issues/issue-868.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_parens)]
// pretty-expanded FIXME #23616

fn f<T, F>(g: F) -> T where F: FnOnce() -> T { g() }

pub fn main() {
  let _x = f( | | { 10 });
    // used to be: cannot determine a type for this expression
    f(| | { });
    // ditto
    f( | | { ()});
    // always worked
    let _: () = f(| | { });
    // empty block with no type info should compile too
    let _ = f(||{});
    let _ = (||{});
}


