tests/ui/issues/issue-4759.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616
#![allow(non_shorthand_field_patterns)]

struct T { a: Box<isize> }

trait U {
    fn f(self);
}

impl U for Box<isize> {
    fn f(self) { }
}

pub fn main() {
    let T { a: a } = T { a: Box::new(0) };
    a.f();
}


