tests/ui/issues/issue-7268.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

fn foo<T: 'static>(_: T) {}

fn bar<T>(x: &'static T) {
    foo(x);
}
fn main() {}


