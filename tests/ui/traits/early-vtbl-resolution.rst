tests/ui/traits/early-vtbl-resolution.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(non_camel_case_types)]
#![allow(dead_code)]
// pretty-expanded FIXME #23616

trait thing<A> {
    fn foo(&self) -> Option<A>;
}
impl<A> thing<A> for isize {
    fn foo(&self) -> Option<A> { None }
}
fn foo_func<A, B: thing<A>>(x: B) -> Option<A> { x.foo() }

struct A { a: isize }

pub fn main() {
    let _x: Option<f64> = foo_func(0);
}


