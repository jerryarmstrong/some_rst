tests/ui/parser/diff-markers/tuple-struct.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S(
<<<<<<< HEAD //~ ERROR encountered diff marker
    u8,
=======
    i8,
>>>>>>> branch
);


