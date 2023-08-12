tests/ui/regions/regions-ret-borrowed-1.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Similar to regions-ret-borrowed.rs, but using a named lifetime.  At
// some point regions-ret-borrowed reported an error but this file did
// not, due to special hardcoding around the anonymous region.

fn with<R, F>(f: F) -> R where F: for<'a> FnOnce(&'a isize) -> R {
    f(&3)
}

fn return_it<'a>() -> &'a isize {
    with(|o| o)
    //~^ ERROR lifetime may not live long enough
}

fn main() {
    let x = return_it();
    println!("foo={}", *x);
}


