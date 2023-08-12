tests/ui/issues/issue-41849-variance-req.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Regression test for #41849.

use std::ops::Mul;

const C: usize = 1;
const CAPACITY: usize = 1 * C;

struct A<X> {
    f: [X; CAPACITY],
}

struct B<T> {
    f: T,
}

impl<T> Mul for B<T> {
    type Output = Self;
    fn mul(self, _rhs: B<T>) -> Self::Output {
        self
    }
}

impl<T> Mul<usize> for B<T> {
    type Output = Self;
    fn mul(self, _rhs: usize) -> Self::Output {
        self
    }
}

fn main() {
    let a = A { f: [1] };
    let _ = B { f: a };
}


