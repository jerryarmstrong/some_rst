tests/ui/binding/fn-pattern-expected-type.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let f = |(x, y): (isize, isize)| {
        assert_eq!(x, 1);
        assert_eq!(y, 2);
    };
    f((1, 2));
}


