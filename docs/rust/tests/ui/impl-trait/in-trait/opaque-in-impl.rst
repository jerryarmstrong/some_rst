tests/ui/impl-trait/in-trait/opaque-in-impl.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

use std::fmt::Debug;

trait Foo {
    fn foo(&self) -> impl Debug;
}

impl Foo for () {
    fn foo(&self) -> impl Debug {
        "Hello, world"
    }
}

impl<T: Default + Debug> Foo for std::marker::PhantomData<T> {
    fn foo(&self) -> impl Debug {
        T::default()
    }
}

trait Bar {
    fn bar<T>(&self) -> impl Debug;
}

impl Bar for () {
    fn bar<T>(&self) -> impl Debug {
        format!("Hello with generic {}", std::any::type_name::<T>())
    }
}

trait Baz {
    fn baz(&self) -> impl Debug + '_;
}

impl Baz for String {
    fn baz(&self) -> impl Debug + '_ {
        (self,)
    }
}

fn main() {
    println!("{:?}", ().foo());
    println!("{:?}", ().bar::<u64>());
    println!("{:?}", "hi".to_string().baz());
}


