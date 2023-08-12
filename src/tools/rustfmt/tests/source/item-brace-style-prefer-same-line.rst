src/tools/rustfmt/tests/source/item-brace-style-prefer-same-line.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-brace_style: PreferSameLine

mod M {
    enum A
    {
        A,
    }

    struct B
    {
        b: i32,
    }

    enum C {}

    struct D {}

    enum A<T> where T: Copy {
        A,
    }

    struct B<T> where T: Copy {
        b: i32,
    }

    enum C<T> where T: Copy {}

    struct D<T> where T: Copy {}
}


