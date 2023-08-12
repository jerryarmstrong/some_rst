tests/ui/regions/regions-infer-call-2.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn takes_two(x: &isize, y: &isize) -> isize { *x + *y }

fn with<T, F>(f: F) -> T where F: FnOnce(&isize) -> T {
    f(&20)
}

fn has_one<'a>(x: &'a isize) -> isize {
    with(|y| takes_two(x, y))
}

pub fn main() {
    assert_eq!(has_one(&2), 22);
}


