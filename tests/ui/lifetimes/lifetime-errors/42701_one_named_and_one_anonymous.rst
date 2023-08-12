tests/ui/lifetimes/lifetime-errors/42701_one_named_and_one_anonymous.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    field: i32,
}

fn foo2<'a>(a: &'a Foo, x: &i32) -> &'a i32 {
    if true {
        let p: &i32 = &a.field;
        &*p
    } else {
        &*x //~ ERROR explicit lifetime
    }
}

fn main() { }


