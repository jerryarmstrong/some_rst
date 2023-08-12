tests/ui/type-alias-impl-trait/wf_check_closures.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

trait Bar {
    fn bar(&self);
}

type FooFn<B> = impl FnOnce();

fn foo<B: Bar>(bar: B) -> FooFn<B> {
    move || { bar.bar() }
    //~^ ERROR the trait bound `B: Bar` is not satisfied
}

fn main() {
    let boom: FooFn<u32> = unsafe { core::mem::zeroed() };
    boom();
}


