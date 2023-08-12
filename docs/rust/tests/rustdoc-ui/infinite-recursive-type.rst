tests/rustdoc-ui/infinite-recursive-type.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum E {
//~^ ERROR recursive type `E` has infinite size
    V(E),
}


