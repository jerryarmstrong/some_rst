tests/ui/const-generics/nested-type.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: full min

#![cfg_attr(full, feature(adt_const_params))]
#![cfg_attr(full, allow(incomplete_features))]

struct Foo<const N: [u8; { //[min]~ ERROR `[u8; _]` is forbidden
    struct Foo<const N: usize>;

    impl<const N: usize> Foo<N> {
        fn value() -> usize {
            N
        }
    }

    Foo::<17>::value()
    //[full]~^ ERROR cannot call non-const fn
}]>;

fn main() {}


