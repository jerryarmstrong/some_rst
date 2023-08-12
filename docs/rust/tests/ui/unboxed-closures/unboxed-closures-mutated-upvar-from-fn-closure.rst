tests/ui/unboxed-closures/unboxed-closures-mutated-upvar-from-fn-closure.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a by-ref `FnMut` closure gets an error when it tries to
// mutate a value.

fn call<F>(f: F) where F : Fn() {
    f();
}

fn main() {
    let mut counter = 0;
    call(|| {
        counter += 1;
        //~^ ERROR cannot assign to `counter`
    });
}


