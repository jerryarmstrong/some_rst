tests/ui/impl-trait/two_tait_defining_each_other3.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type A = impl Foo;
type B = impl Foo;

trait Foo {}

fn muh(x: A) -> B {
    if false {
        return x;  // B's hidden type is A (opaquely)
        //~^ ERROR opaque type's hidden type cannot be another opaque type
    }
    Bar // A's hidden type is `Bar`, because all the return types are compared with each other
}

struct Bar;
impl Foo for Bar {}

fn main() {}


