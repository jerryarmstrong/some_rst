src/tools/rustfmt/tests/target/issue-4310.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_generics)]

fn foo<
    const N: [u8; {
        struct Inner<'a>(&'a ());
        3
    }],
>() {
}


