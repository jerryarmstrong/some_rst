src/tools/miri/tests/pass/tuple_like_struct_constructor.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    #[derive(PartialEq, Eq, Debug)]
    struct A(i32);
    assert_eq!(Some(42).map(A), Some(A(42)));
}


