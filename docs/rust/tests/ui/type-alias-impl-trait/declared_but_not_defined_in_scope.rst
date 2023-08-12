tests/ui/type-alias-impl-trait/declared_but_not_defined_in_scope.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

mod boo {
    // declared in module but not defined inside of it
    pub type Boo = impl ::std::fmt::Debug; //~ ERROR unconstrained opaque type
}

fn bomp() -> boo::Boo {
    ""
    //~^ mismatched types
}


