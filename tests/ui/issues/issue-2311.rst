tests/ui/issues/issue-2311.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(non_camel_case_types)]

// pretty-expanded FIXME #23616

trait clam<A> { fn get(self) -> A; }
trait foo<A> {
   fn bar<B,C:clam<A>>(&self, c: C) -> B;
}

pub fn main() { }


