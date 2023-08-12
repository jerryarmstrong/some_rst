src/tools/clippy/tests/ui-toml/vec_box_sized/test.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    x: u64,
}

struct C {
    y: u16,
}

struct Foo(Vec<Box<u8>>);
struct Bar(Vec<Box<u16>>);
struct Quux(Vec<Box<u32>>);
struct Baz(Vec<Box<(u16, u16)>>);
struct BarBaz(Vec<Box<S>>);
struct FooBarBaz(Vec<Box<C>>);

fn main() {}


