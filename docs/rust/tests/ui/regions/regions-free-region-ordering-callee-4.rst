tests/ui/regions/regions-free-region-ordering-callee-4.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that callees correctly infer an ordering between free regions
// that appear in their parameter list.  See also
// regions-free-region-ordering-caller.rs

fn ordering4<'a, 'b, F>(a: &'a usize, b: &'b usize, x: F) where F: FnOnce(&'a &'b usize) {
    //~^ ERROR reference has a longer lifetime than the data it references
    // Do not infer ordering from closure argument types.
    let z: Option<&'a &'b usize> = None;
}

fn main() {}


