tests/ui/fun-indirect-call.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f() -> isize { return 42; }

pub fn main() {
    let g: fn() -> isize = f;
    let i: isize = g();
    assert_eq!(i, 42);
}


