tests/ui/suggestions/impl-trait-with-missing-trait-bounds-in-arg.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

trait Foo {}

trait Bar {
    fn hello(&self) {}
}

struct S;

impl Foo for S {}
impl Bar for S {}

fn test(foo: impl Foo) {
    foo.hello(); //~ ERROR E0599
}

fn main() {
    test(S);
}


