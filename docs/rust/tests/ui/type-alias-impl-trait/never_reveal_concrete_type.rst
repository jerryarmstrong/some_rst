tests/ui/type-alias-impl-trait/never_reveal_concrete_type.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]
// check-pass
fn main() {}

type NoReveal = impl std::fmt::Debug;

fn define_no_reveal() -> NoReveal {
    ""
}

fn no_reveal(x: NoReveal) {
    let _: &'static str = x;
    let _ = x as &'static str;
}


