tests/ui/functions-closures/closure-returning-closure.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn main() {
    let f = |_||x, y| x+y;
    assert_eq!(f(())(1, 2), 3);
}


