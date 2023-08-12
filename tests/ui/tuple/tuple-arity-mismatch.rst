tests/ui/tuple/tuple-arity-mismatch.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #6155

fn first((value, _): (isize, f64)) -> isize { value }

fn main() {
    let y = first ((1,2.0,3));
    //~^ ERROR mismatched types
    //~| expected tuple `(isize, f64)`
    //~| found tuple `(isize, f64, {integer})`
    //~| expected a tuple with 2 elements, found one with 3 elements

    let y = first ((1,));
    //~^ ERROR mismatched types
    //~| expected tuple `(isize, f64)`
    //~| found tuple `(isize,)`
    //~| expected a tuple with 2 elements, found one with 1 element
}


