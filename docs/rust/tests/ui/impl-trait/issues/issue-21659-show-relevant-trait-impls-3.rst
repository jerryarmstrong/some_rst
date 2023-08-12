tests/ui/impl-trait/issues/issue-21659-show-relevant-trait-impls-3.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo<A> {
    fn foo(&self, a: A) -> A {
        a
    }
}

trait NotRelevant<A> {
    fn nr(&self, a: A) -> A {
        a
    }
}

struct Bar;

impl NotRelevant<usize> for Bar {}

fn main() {
    let f1 = Bar;

    f1.foo(1usize);
    //~^ error: method named `foo` found for struct `Bar` in the current scope
}


