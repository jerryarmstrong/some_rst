tests/ui/struct-ctor-mangling.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn size_of_val<T>(_: &T) -> usize {
    std::mem::size_of::<T>()
}

struct Foo(#[allow(unused_tuple_struct_fields)] i64);

// Test that the (symbol) mangling of `Foo` (the `struct` type) and that of
// `typeof Foo` (the function type of the `struct` constructor) don't collide.
fn main() {
    size_of_val(&Foo(0));
    size_of_val(&Foo);
}


