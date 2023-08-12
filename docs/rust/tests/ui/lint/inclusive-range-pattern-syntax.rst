tests/ui/lint/inclusive-range-pattern-syntax.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// run-rustfix

#![warn(ellipsis_inclusive_range_patterns)]

fn main() {
    let despondency = 2;
    match despondency {
        1...2 => {}
        //~^ WARN `...` range patterns are deprecated
        //~| WARN this is accepted in the current edition
        _ => {}
    }

    match &despondency {
        &1...2 => {}
        //~^ WARN `...` range patterns are deprecated
        //~| WARN this is accepted in the current edition
        _ => {}
    }
}


