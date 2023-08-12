tests/ui/recursion/recursive-requirements.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::marker::PhantomData;

struct AssertSync<T: Sync>(PhantomData<T>);

pub struct Foo {
    bar: *const Bar,
    phantom: PhantomData<Bar>,
}

pub struct Bar {
    foo: *const Foo,
    phantom: PhantomData<Foo>,
}

fn main() {
    let _: AssertSync<Foo> = unimplemented!();
    //~^ ERROR E0277
    //~| ERROR E0277
}


