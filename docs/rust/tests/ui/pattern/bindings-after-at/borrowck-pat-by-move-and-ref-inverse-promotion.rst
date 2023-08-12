tests/ui/pattern/bindings-after-at/borrowck-pat-by-move-and-ref-inverse-promotion.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `by_move_binding @ pat_with_by_ref_bindings` is prevented even with promotion.
// Currently this logic exists in THIR match checking as opposed to borrowck.

fn main() {
    struct U;
    let a @ ref b = U; //~ ERROR borrow of moved value
}


