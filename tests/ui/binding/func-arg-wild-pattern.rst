tests/ui/binding/func-arg-wild-pattern.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that we can compile code that uses a `_` in function argument
// patterns.


fn foo((x, _): (isize, isize)) -> isize {
    x
}

pub fn main() {
    assert_eq!(foo((22, 23)), 22);
}


