tests/ui/parser/diff-markers/struct.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
<<<<<<< HEAD //~ ERROR encountered diff marker
    x: u8,
=======
    x: i8,
>>>>>>> branch
}


