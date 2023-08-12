tests/ui/span/borrowck-fn-in-const-b.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we check fns appearing in constant declarations.
// Issue #22382.

// How about mutating an immutable vector?
const MUTATE: fn(&Vec<String>) = {
    fn broken(x: &Vec<String>) {
        x.push(format!("this is broken"));
        //~^ ERROR cannot borrow
    }
    broken
};

fn main() {
}


