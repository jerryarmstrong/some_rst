tests/ui/moves/suggest-clone.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#[derive(Clone)]
struct Foo;
impl Foo {
    fn foo(self) {}
}
fn main() {
    let foo = &Foo;
    foo.foo(); //~ ERROR cannot move out
}


