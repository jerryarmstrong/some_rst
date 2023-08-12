tests/ui/closures/2229_closure_analysis/diagnostics/borrowck/borrowck-3.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

#[derive(Debug)]
struct Point {
    x: String,
    y: String,
}
fn main() {
    let mut c = {
        let mut p = Point {x: "1".to_string(), y: "2".to_string() };
        || { //~ ERROR closure may outlive the current block, but it borrows `p`
           let x = &mut p.x;
           println!("{:?}", p);
        }
    };
    c();
}


