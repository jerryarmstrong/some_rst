tests/ui/extern/extern-wrong-value-type.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" fn f() {
}

fn is_fn<F>(_: F) where F: Fn() {}

fn main() {
    // extern functions are extern "C" fn
    let _x: extern "C" fn() = f; // OK
    is_fn(f);
    //~^ ERROR expected a `Fn<()>` closure, found `extern "C" fn() {f}`
}


