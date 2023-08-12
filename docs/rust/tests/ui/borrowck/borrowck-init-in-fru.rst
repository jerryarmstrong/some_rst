tests/ui/borrowck/borrowck-init-in-fru.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Clone)]
struct Point {
    x: isize,
    y: isize,
}

fn main() {
    let mut origin: Point;
    origin = Point { x: 10, ..origin };
    //~^ ERROR E0381
    origin.clone();
}


