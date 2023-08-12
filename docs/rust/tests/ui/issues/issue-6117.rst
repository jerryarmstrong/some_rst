tests/ui/issues/issue-6117.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

enum Either<T, U> { Left(T), Right(U) }

pub fn main() {
    match Either::Left(Box::new(17)) {
        Either::Right(()) => {}
        _ => {}
    }
}


