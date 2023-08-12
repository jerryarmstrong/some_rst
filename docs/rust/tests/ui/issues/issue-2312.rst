tests/ui/issues/issue-2312.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

// Testing that the B's are resolved


trait clam<A> { fn get(self) -> A; }

struct foo(isize);

impl foo {
    pub fn bar<B,C:clam<B>>(&self, _c: C) -> B { panic!(); }
}

pub fn main() { }


