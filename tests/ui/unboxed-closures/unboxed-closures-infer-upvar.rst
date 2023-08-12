tests/ui/unboxed-closures/unboxed-closures-infer-upvar.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that the type variable in the type(`Vec<_>`) of a closed over
// variable does not interfere with type inference.

fn f<F: FnMut()>(mut f: F) {
    f();
}

fn main() {
    let mut v: Vec<_> = vec![];
    f(|| v.push(0));
    assert_eq!(v, [0]);
}


