tests/ui/closures/2229_closure_analysis/diagnostics/borrowck/borrowck-2.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}
fn main() {
    let mut p = Point {x: 1, y: 2 };

    let y = &p.y;
    let mut c = || {
    //~^ ERROR cannot borrow `p` as mutable because it is also borrowed as immutable
       println!("{:?}", p);
       let x = &mut p.x;
    };
    c();
    println!("{}", y);
}


