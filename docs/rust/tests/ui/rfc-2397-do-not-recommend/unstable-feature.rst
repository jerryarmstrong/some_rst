tests/ui/rfc-2397-do-not-recommend/unstable-feature.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
}

#[do_not_recommend]
//~^ ERROR the `#[do_not_recommend]` attribute is an experimental feature
impl Foo for i32 {
}

fn main() {
}


