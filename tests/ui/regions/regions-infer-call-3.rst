tests/ui/regions/regions-infer-call-3.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn select<'r>(x: &'r isize, y: &'r isize) -> &'r isize { x }

fn with<T, F>(f: F) -> T where F: FnOnce(&isize) -> T {
    f(&20)
}

fn manip<'a>(x: &'a isize) -> isize {
    let z = with(|y| { select(x, y) });
    //~^ ERROR lifetime may not live long enough
    *z
}

fn main() {
}


