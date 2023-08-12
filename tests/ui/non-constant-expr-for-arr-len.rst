tests/ui/non-constant-expr-for-arr-len.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that non constant exprs fail for array repeat syntax

fn main() {
    fn bar(n: usize) {
        let _x = [0; n];
        //~^ ERROR attempt to use a non-constant value in a constant [E0435]
    }
}


