tests/ui/const-generics/generic_const_exprs/assoc_const_unification/const_equate_assoc_consts.rs
================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

trait Trait {
    const ASSOC: usize;
}
impl<T> Trait for T {
    const ASSOC: usize = std::mem::size_of::<T>();
}

struct Foo<T: Trait>([u8; T::ASSOC])
where
    [(); T::ASSOC]:;

fn bar<T: Trait>()
where
    [(); T::ASSOC]:,
{
    let _: Foo<T> = Foo::<_>(make());
}

fn make() -> ! {
    todo!()
}

fn main() {}


