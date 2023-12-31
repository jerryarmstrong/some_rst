tests/ui/impl-trait/hidden-type-is-opaque-2.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This doesn't work, because we don't flow information from opaque types
// into function arguments via the function's generic parameters
// FIXME(oli-obk): make `expected_inputs_for_expected_output` support this

#![feature(type_alias_impl_trait)]

fn reify_as() -> Thunk<impl FnOnce(Continuation) -> Continuation> {
    Thunk::new(|mut cont| {
        cont.reify_as(); //~ ERROR type annotations needed
        cont
    })
}

type Tait = impl FnOnce(Continuation) -> Continuation;

fn reify_as_tait() -> Thunk<Tait> {
    Thunk::new(|mut cont| {
        cont.reify_as(); //~ ERROR type annotations needed
        cont
    })
}

#[must_use]
struct Thunk<F>(F);

impl<F> Thunk<F> {
    fn new(f: F) -> Self
    where
        F: ContFn,
    {
        Thunk(f)
    }
}

trait ContFn {}

impl<F: FnOnce(Continuation) -> Continuation> ContFn for F {}

struct Continuation;

impl Continuation {
    fn reify_as(&mut self) {}
}

fn main() {}


