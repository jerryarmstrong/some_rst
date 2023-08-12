tests/ui/closures/closure-bounds-cant-promote-superkind-in-struct.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct X<F> where F: FnOnce() + 'static + Send {
    field: F,
}

fn foo<F>(blk: F) -> X<F> where F: FnOnce() + 'static {
    //~^ ERROR `F` cannot be sent between threads safely
    return X { field: blk };
}

fn main() {
}


