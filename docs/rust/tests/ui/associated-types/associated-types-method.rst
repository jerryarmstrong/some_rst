tests/ui/associated-types/associated-types-method.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that methods whose impl-trait-ref contains associated types
// are supported.

trait Device {
    type Resources;
}
#[allow(unused_tuple_struct_fields)]
struct Foo<D, R>(D, R);

trait Tr {
    fn present(&self) {}
}

impl<D: Device> Tr for Foo<D, D::Resources> {
    fn present(&self) {}
}

struct Res;
struct Dev;
impl Device for Dev {
    type Resources = Res;
}

fn main() {
    let foo = Foo(Dev, Res);
    foo.present();
}


