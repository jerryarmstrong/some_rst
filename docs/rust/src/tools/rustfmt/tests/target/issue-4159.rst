src/tools/rustfmt/tests/target/issue-4159.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    type A: Ord;

    type A<'a>
    where
        'a: 'static;

    type A<T: Ord>
    where
        T: 'static;

    type A = u8;

    type A<'a: 'static, T: Ord + 'static>: Eq + PartialEq
    where
        T: 'static + Copy,
    = Vec<u8>;
}


