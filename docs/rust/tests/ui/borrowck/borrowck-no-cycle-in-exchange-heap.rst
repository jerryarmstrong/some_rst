tests/ui/borrowck/borrowck-no-cycle-in-exchange-heap.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Node_ {
    a: Box<Cycle>
}

enum Cycle {
    Node(Node_),
    Empty,
}

fn main() {
    let mut x: Box<_> = Box::new(Cycle::Node(Node_ {a: Box::new(Cycle::Empty)}));

    // Create a cycle!
    match *x {
      Cycle::Node(ref mut y) => {
        y.a = x; //~ ERROR cannot move out of
      }
      Cycle::Empty => {}
    };
}


