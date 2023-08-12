tests/ui/issues/issue-2284.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

trait Send {
    fn f(&self);
}

fn f<T:Send>(t: T) {
    t.f();
}

pub fn main() {
}


