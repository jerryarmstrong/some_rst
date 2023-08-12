tests/ui/deriving/deriving-clone-generic-enum.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

#[derive(Clone)]
enum E<T,U> {
    A(T),
    B(T,U),
    C
}

pub fn main() {
    let _ = E::A::<isize, isize>(1).clone();
}


