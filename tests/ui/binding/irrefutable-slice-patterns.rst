tests/ui/binding/irrefutable-slice-patterns.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Regression test for #47096.

fn foo(s: &[i32]) -> &[i32] {
    let &[ref xs @ ..] = s;
    xs
}

fn main() {
    let x = [1, 2, 3];
    let y = foo(&x);
    assert_eq!(x, y);
}


