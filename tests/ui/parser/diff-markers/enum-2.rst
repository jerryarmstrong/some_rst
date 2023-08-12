tests/ui/parser/diff-markers/enum-2.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum E {
    Foo {
<<<<<<< HEAD //~ ERROR encountered diff marker
        x: u8,
|||||||
        z: (),
=======
        y: i8,
>>>>>>> branch
    }
}


