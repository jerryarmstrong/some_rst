src/tools/rustfmt/tests/target/item-brace-style-same-line-where.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod M {
    enum A {
        A,
    }

    struct B {
        b: i32,
    }

    // For empty enums and structs, the brace remains on the same line.
    enum C {}

    struct D {}

    enum A<T>
    where
        T: Copy,
    {
        A,
    }

    struct B<T>
    where
        T: Copy,
    {
        b: i32,
    }

    // For empty enums and structs, the brace remains on the same line.
    enum C<T>
    where
        T: Copy, {}

    struct D<T>
    where
        T: Copy, {}
}


