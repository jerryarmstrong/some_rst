tests/ui/for-loop-while/for-destruct.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Pair { x: isize, y: isize }

pub fn main() {
    for elt in &(vec![Pair {x: 10, y: 20}, Pair {x: 30, y: 0}]) {
        assert_eq!(elt.x + elt.y, 30);
    }
}


