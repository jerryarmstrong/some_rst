tests/ui/generics/generic-type.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass



struct Pair<T> {x: T, y: T}

pub fn main() {
    let x: Pair<isize> = Pair {x: 10, y: 12};
    assert_eq!(x.x, 10);
    assert_eq!(x.y, 12);
}


