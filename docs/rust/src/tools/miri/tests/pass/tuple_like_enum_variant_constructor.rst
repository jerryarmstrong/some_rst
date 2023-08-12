src/tools/miri/tests/pass/tuple_like_enum_variant_constructor.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    assert_eq!(Some(42).map(Some), Some(Some(42)));
}


