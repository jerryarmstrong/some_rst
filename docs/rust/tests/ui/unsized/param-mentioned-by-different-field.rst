tests/ui/unsized/param-mentioned-by-different-field.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // We must not allow this with our current setup as `T`
// is mentioned both in the tail of `Foo` and by another
// field.
struct Foo<T: ?Sized>(Box<T>, T);

fn main() {
    let x: Foo<[u8; 1]> = Foo(Box::new([2]), [3]);
    let y: &Foo<[u8]> = &x; //~ ERROR mismatched types
    assert_eq!(y.0.len(), 1);
}


