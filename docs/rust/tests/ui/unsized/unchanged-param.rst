tests/ui/unsized/unchanged-param.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that we allow unsizing even if there is an unchanged param in the
// field getting unsized.
struct A<T, U: ?Sized + 'static>(#[allow(unused_tuple_struct_fields)] T, B<T, U>);
struct B<T, U: ?Sized>(#[allow(unused_tuple_struct_fields)] T, U);

fn main() {
    let x: A<[u32; 1], [u32; 1]> = A([0; 1], B([0; 1], [0; 1]));
    let y: &A<[u32; 1], [u32]> = &x;
    assert_eq!(y.1.1.len(), 1);
}


