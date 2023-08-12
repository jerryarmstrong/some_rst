tests/ui/resolve/unresolved_static_type_field.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f(_: bool) {}

struct Foo {
    cx: bool,
}

impl Foo {
    fn bar() {
        f(cx);
        //~^ ERROR cannot find value `cx` in this scope
    }
}

fn main() {}


