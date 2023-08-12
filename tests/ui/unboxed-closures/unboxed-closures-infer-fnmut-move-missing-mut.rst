tests/ui/unboxed-closures/unboxed-closures-infer-fnmut-move-missing-mut.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we are able to infer a suitable kind for this closure
// that is just called (`FnMut`).

fn main() {
    let mut counter = 0;
    let tick = move || counter += 1;
    tick(); //~ ERROR cannot borrow `tick` as mutable, as it is not declared as mutable
}


