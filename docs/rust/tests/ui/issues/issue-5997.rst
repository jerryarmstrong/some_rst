tests/ui/issues/issue-5997.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

fn f<T>() -> bool {
    enum E<T> { V(T) }

    struct S<T>(T);

    true
}

fn main() {
    let b = f::<isize>();
    assert!(b);
}


