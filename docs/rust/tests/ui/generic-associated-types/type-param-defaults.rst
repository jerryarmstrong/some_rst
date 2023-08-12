tests/ui/generic-associated-types/type-param-defaults.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we disallow GAT param defaults, even with `invalid_type_param_default` allowed

#![allow(invalid_type_param_default)]

trait Trait {
    type Assoc<T = u32>;
    //~^ defaults for type parameters are only allowed
}

impl Trait for () {
    type Assoc<T = u32> = u64;
    //~^ defaults for type parameters are only allowed
}

impl Trait for u32 {
    type Assoc<T = u32> = T;
    //~^ defaults for type parameters are only allowed
}

trait Other {}
impl Other for u32 {}

fn foo<T>()
where
    T: Trait<Assoc = u32>,
    T::Assoc: Other {
    }

fn main() {
    // errors
    foo::<()>();
    // works
    foo::<u32>();
}


