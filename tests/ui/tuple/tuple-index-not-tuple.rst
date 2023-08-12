tests/ui/tuple/tuple-index-not-tuple.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Point { x: isize, y: isize }
struct Empty;

fn main() {
    let origin = Point { x: 0, y: 0 };
    origin.0;
    //~^ ERROR no field `0` on type `Point`
    Empty.0;
    //~^ ERROR no field `0` on type `Empty`
}


