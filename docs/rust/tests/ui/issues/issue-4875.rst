tests/ui/issues/issue-4875.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// regression test for issue 4875

// pretty-expanded FIXME #23616

pub struct Foo<T> {
    data: T,
}

fn foo<T>(Foo{..}: Foo<T>) {
}

pub fn main() {
}


