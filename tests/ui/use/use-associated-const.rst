tests/ui/use/use-associated-const.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_imports)]

pub mod foo {
    pub struct Foo;

    impl Foo {
        pub const BAR: i32 = 0;
    }
}

use foo::Foo::BAR; //~ ERROR unresolved import `foo::Foo`

fn main() {}


