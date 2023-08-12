tests/ui/pattern/issue-17718-patterns.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static A1: usize = 1;
static mut A2: usize = 1;
const A3: usize = 1;

fn main() {
    match 1 {
        A1 => {} //~ ERROR: match bindings cannot shadow statics
        A2 => {} //~ ERROR: match bindings cannot shadow statics
        A3 => {}
        _ => {}
    }
}


