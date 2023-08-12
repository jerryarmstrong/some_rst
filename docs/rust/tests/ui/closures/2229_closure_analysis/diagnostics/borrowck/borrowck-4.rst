tests/ui/closures/2229_closure_analysis/diagnostics/borrowck/borrowck-4.rs
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
fn foo () -> impl FnMut()->() {
    let mut p = Point {x: 1, y: 2 };
    let mut c = || {
    //~^ ERROR closure may outlive the current function, but it borrows `p`
       p.x+=5;
       println!("{:?}", p);
    };
    c
}
fn main() {
    let c = foo();
    c();
}


