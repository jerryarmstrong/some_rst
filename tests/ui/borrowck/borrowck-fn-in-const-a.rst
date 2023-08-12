tests/ui/borrowck/borrowck-fn-in-const-a.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we check fns appearing in constant declarations.
// Issue #22382.

const MOVE: fn(&String) -> String = {
    fn broken(x: &String) -> String {
        return *x //~ ERROR cannot move
    }
    broken
};

fn main() {
}


