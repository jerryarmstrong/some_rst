tests/ui/type-alias-impl-trait/not_a_defining_use.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

use std::fmt::Debug;

fn main() {}

type Two<T, U> = impl Debug;

fn three<T: Debug, U>(t: T) -> Two<T, U> {
    (t, 5i8)
    //~^ ERROR `T` doesn't implement `Debug`
}

trait Bar {
    type Blub: Debug;
    const FOO: Self::Blub;
}

impl Bar for u32 {
    type Blub = i32;
    const FOO: i32 = 42;
}

fn four<T: Debug, U: Bar>(t: T) -> Two<T, U> {
    (t, <U as Bar>::FOO)
    //~^ ERROR `U: Bar` is not satisfied
    //~| ERROR `T` doesn't implement `Debug`
}

fn is_sync<T: Sync>() {}

fn asdfl() {
    //FIXME(oli-obk): these currently cause cycle errors
    //is_sync::<Two<i32, u32>>();
    //is_sync::<Two<i32, *const i32>>();
}


