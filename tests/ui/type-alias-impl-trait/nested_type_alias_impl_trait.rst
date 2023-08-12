tests/ui/type-alias-impl-trait/nested_type_alias_impl_trait.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

mod my_mod {
    use std::fmt::Debug;

    pub type Foo = impl Debug;
    pub type Foot = impl Debug;

    pub fn get_foo() -> Foo {
        5i32
    }

    pub fn get_foot() -> Foot {
        get_foo() //~ ERROR opaque type's hidden type cannot be another opaque type
    }
}

fn main() {
    let _: my_mod::Foot = my_mod::get_foot();
}


