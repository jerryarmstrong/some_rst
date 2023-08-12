tests/ui/wf/wf-outlives-ty-in-fn-or-trait.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]
#![allow(dead_code)]

trait Trait<'a, T> {
    type Out;
}

impl<'a, T> Trait<'a, T> for usize {
    type Out = &'a fn(T); //~ ERROR `T` may not live long enough
}

struct Foo<'a,T> {
    f: &'a fn(T),
}

trait Baz<T> { }

impl<'a, T> Trait<'a, T> for u32 {
    type Out = &'a dyn Baz<T>; //~ ERROR `T` may not live long enough
}

fn main() { }


