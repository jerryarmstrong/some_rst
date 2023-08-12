tests/ui/const-generics/inhabited-assoc-ty-ice-1.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

// This tests that the inhabited check doesn't cause
// ICEs by trying to evaluate `T::ASSOC` with an incorrect `ParamEnv`.

trait Foo {
    const ASSOC: usize = 1;
}

#[allow(unused_tuple_struct_fields)]
struct Iced<T: Foo>(T, [(); T::ASSOC])
where
    [(); T::ASSOC]: ;

impl Foo for u32 {}

fn foo<T: Foo>()
where
    [(); T::ASSOC]: ,
{
    let _iced: Iced<T> = return;
}

fn main() {
    foo::<u32>();
}


