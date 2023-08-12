tests/ui/mismatched_types/closure-arg-count-expected-type-issue-47244.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #47244: in this specific scenario, when the
// expected type indicated 1 argument but the closure takes two, we
// would (early on) create type variables for the type of `b`. If the
// user then attempts to invoke a method on `b`, we would get an error
// saying that the type of `b` must be known, which was not very
// helpful.

// run-rustfix

use std::collections::HashMap;

fn main() {
    let mut m = HashMap::new();
    m.insert("foo", "bar");

    let _n = m.iter().map(|_, b| {
        //~^ ERROR closure is expected to take a single 2-tuple
        b.to_string()
    });
}


