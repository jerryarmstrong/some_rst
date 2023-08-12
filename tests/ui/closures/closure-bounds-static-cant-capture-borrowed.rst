tests/ui/closures/closure-bounds-static-cant-capture-borrowed.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn bar<F>(blk: F) where F: FnOnce() + 'static {
}

fn foo(x: &()) {
    bar(|| {
        //~^ ERROR borrowed data escapes
        //~| ERROR closure may outlive
        let _ = x;
    })
}

fn main() {
}


