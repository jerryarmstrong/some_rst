tests/ui/type-alias-impl-trait/no_revealing_outside_defining_module.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

mod boo {
    pub type Boo = impl ::std::fmt::Debug;
    fn bomp() -> Boo {
        ""
    }
}

// We don't actually know the type here.

fn bomp2() {
    let _: &str = bomp(); //~ ERROR mismatched types
}

fn bomp() -> boo::Boo {
    "" //~ ERROR mismatched types
}

fn bomp_loop() -> boo::Boo {
    loop {}
}


