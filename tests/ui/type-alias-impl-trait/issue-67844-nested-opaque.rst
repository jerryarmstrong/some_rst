tests/ui/type-alias-impl-trait/issue-67844-nested-opaque.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Regression test for issue #67844
// Ensures that we properly handle nested TAIT occurrences
// with generic parameters

#![feature(type_alias_impl_trait)]

trait WithAssoc {
    type AssocType;
}

trait WithParam<A> {}

type Return<A> = impl WithAssoc<AssocType = impl WithParam<A>>;

struct MyParam;
impl<A> WithParam<A> for MyParam {}

struct MyStruct;

impl WithAssoc for MyStruct {
    type AssocType = MyParam;
}

fn my_fun<A>() -> Return<A> {
    MyStruct
}

fn my_other_fn<A>() -> impl WithAssoc<AssocType = impl WithParam<A>> {
    MyStruct
}

fn main() {}


