tests/ui/regions/region-bound-on-closure-outlives-call.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn call_rec<F>(mut f: F) -> usize where F: FnMut(usize) -> usize {
    //~^ WARN function cannot return without recursing
    (|x| f(x))(call_rec(f)) //~ ERROR cannot move out of `f`
}

fn main() {}


