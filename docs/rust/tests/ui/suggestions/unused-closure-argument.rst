tests/ui/suggestions/unused-closure-argument.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_variables)]

struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let points = vec!(Point { x: 1, y: 2 }, Point { x: 3, y: 4 });

    let _: i32 = points.iter()
        .map(|Point { x, y }| y)
        //~^ ERROR unused variable
        .sum();

    let _: i32 = points.iter()
        .map(|x| 4)
        //~^ ERROR unused variable
        .sum();
}


