tests/ui/impl-trait/two_tait_defining_each_other2.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type A = impl Foo; //~ ERROR unconstrained opaque type
type B = impl Foo;

trait Foo {}

fn muh(x: A) -> B {
    x // B's hidden type is A (opaquely)
    //~^ ERROR opaque type's hidden type cannot be another opaque type
}

struct Bar;
impl Foo for Bar {}

fn main() {}


