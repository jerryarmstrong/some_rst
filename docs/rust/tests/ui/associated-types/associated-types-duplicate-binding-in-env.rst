tests/ui/associated-types/associated-types-duplicate-binding-in-env.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Check that we do not report ambiguities when the same predicate
// appears in the environment twice. Issue #21965.

// pretty-expanded FIXME #23616

trait Foo {
    type B;

    fn get() -> Self::B;
}

fn foo<T>() -> ()
    where T : Foo<B=()>, T : Foo<B=()>
{
    <T as Foo>::get()
}

fn main() {
}


