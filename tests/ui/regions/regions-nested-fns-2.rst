tests/ui/regions/regions-nested-fns-2.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn ignore<F>(_f: F) where F: for<'z> FnOnce(&'z isize) -> &'z isize {}

fn nested() {
    let y = 3;
    ignore(
        |z| {
            if false { &y } else { z }
            //~^ ERROR `y` does not live long enough
        });
}

fn main() {}


