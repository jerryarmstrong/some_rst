tests/ui/type-alias-impl-trait/wf-check-fn-def.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

trait Bar {
    fn bar(&self);
}

type FooFn<B> = impl FnOnce(B);

fn foo<B: Bar>() -> FooFn<B> {
    fn mop<B: Bar>(bar: B) { bar.bar() }
    mop // NOTE: no function pointer, but function zst item
    //~^ ERROR the trait bound `B: Bar` is not satisfied
}

fn main() {
    let boom: FooFn<u32> = unsafe { core::mem::zeroed() };
    boom(42);
}


