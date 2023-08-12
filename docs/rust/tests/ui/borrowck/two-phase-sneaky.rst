tests/ui/borrowck/two-phase-sneaky.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This is the first counter-example from Niko's blog post
// smallcultfollowing.com/babysteps/blog/2017/03/01/nested-method-calls-via-two-phase-borrowing/
// of a danger for code to crash if we just turned off the check for whether
// a mutable-borrow aliases another borrow.

fn main() {
    let mut v: Vec<String> = vec![format!("Hello, ")];
    v[0].push_str({

        v.push(format!("foo"));
        //~^   ERROR cannot borrow `v` as mutable more than once at a time [E0499]

        "World!"
    });
}


