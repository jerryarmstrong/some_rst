tests/ui/parser/diff-markers/struct-expr.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    x: u8,
}
fn main() {
    let _ = S {
<<<<<<< HEAD //~ ERROR encountered diff marker
        x: 42,
=======
        x: 0,
>>>>>>> branch
    }
}


