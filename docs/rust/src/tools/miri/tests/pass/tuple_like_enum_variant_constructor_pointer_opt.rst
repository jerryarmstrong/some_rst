src/tools/miri/tests/pass/tuple_like_enum_variant_constructor_pointer_opt.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = 5;
    assert_eq!(Some(&x).map(Some), Some(Some(&x)));
}


