tests/ui/closures/2229_closure_analysis/run_pass/destructure-pattern-closure-within-closure.rs
==============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// check-pass
#![warn(unused)]

fn main() {
    let t = (String::from("Hello"), String::from("World"));
    let g = (String::from("Mr"), String::from("Goose"));

    let a = || {
        let (_, g2) = g;
        //~^ WARN unused variable: `g2`
        let c = ||  {
            let (_, t2) = t;
            //~^ WARN unused variable: `t2`
        };

        c();
    };

    a();
}


