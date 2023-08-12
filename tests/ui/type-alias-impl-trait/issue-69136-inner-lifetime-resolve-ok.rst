tests/ui/type-alias-impl-trait/issue-69136-inner-lifetime-resolve-ok.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test-pass variant of #69136

// check-pass

#![feature(type_alias_impl_trait)]

trait SomeTrait {}

impl SomeTrait for () {}

trait WithAssoc {
    type AssocType;
}

impl WithAssoc for () {
    type AssocType = ();
}

type Return<'a> = impl WithAssoc<AssocType = impl Sized + 'a>;

fn my_fun<'a>() -> Return<'a> {}

fn main() {}


