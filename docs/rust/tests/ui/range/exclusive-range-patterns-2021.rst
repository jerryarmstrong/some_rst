tests/ui/range/exclusive-range-patterns-2021.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

fn main() {
    let n = 2;
    match n {
        0...3 => {}
        //~^ ERROR `...` range patterns are deprecated
        4...10 => {}
        //~^ ERROR `...` range patterns are deprecated
        (11...100) => {}
        //~^ ERROR `...` range patterns are deprecated
        _ => {}
    }
}


