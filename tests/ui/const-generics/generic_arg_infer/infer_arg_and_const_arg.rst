tests/ui/const-generics/generic_arg_infer/infer_arg_and_const_arg.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_arg_infer)]

struct Foo<const N: bool, const M: u8>;
struct Bar<const N: u8, const M: u32>;

fn main() {
    let _: Foo<true, _> = Foo::<_, 1>;
    let _: Foo<_, 1> = Foo::<true, _>;
    let _: Bar<1, _> = Bar::<_, 300>;
    let _: Bar<_, 300> = Bar::<1, _>;
}


