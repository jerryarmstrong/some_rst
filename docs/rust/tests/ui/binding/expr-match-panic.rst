tests/ui/binding/expr-match-panic.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


fn test_simple() {
    let r = match true { true => { true } false => { panic!() } };
    assert_eq!(r, true);
}

fn test_box() {
    let r = match true { true => { vec![10] } false => { panic!() } };
    assert_eq!(r[0], 10);
}

pub fn main() { test_simple(); test_box(); }


