tests/ui/parser/diff-markers/enum.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum E {
<<<<<<< HEAD //~ ERROR encountered diff marker
    Foo(u8),
=======
    Bar(i8),
>>>>>>> branch
}


