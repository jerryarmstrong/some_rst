tests/ui/type-alias-impl-trait/bound_reduction.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![allow(warnings)]
#![feature(type_alias_impl_trait)]

fn main() {
}

type Foo<V> = impl std::fmt::Debug;

trait Trait<U> {}

fn foo_desugared<T: Trait<[u32; {
    #[no_mangle]
    static FOO: usize = 42;
    3
}]>>(_: T) -> Foo<T> {
    (42, std::marker::PhantomData::<T>)
}


