tests/ui/traits/default-method/bound-subst4.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]


trait A<T> {
    fn g(&self, x: usize) -> usize { x }
    fn h(&self, x: T) { }
}

impl<T> A<T> for isize { }

fn f<T, V: A<T>>(i: V, j: usize) -> usize {
    i.g(j)
}

pub fn main () {
    assert_eq!(f::<f64, isize>(0, 2), 2);
    assert_eq!(f::<usize, isize>(0, 2), 2);
}


