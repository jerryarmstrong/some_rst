tests/rustdoc-ui/infinite-recursive-type-impl-trait.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn f() -> impl Sized {
    // rustdoc doesn't care that this is infinitely sized
    enum E {
        V(E),
    }
    unimplemented!()
}


