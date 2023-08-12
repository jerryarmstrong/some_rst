tests/ui/typeck/issue-87872-missing-inaccessible-field-pattern.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code, unused_variables)]

pub mod foo {
    #[derive(Default)]
    pub struct Foo { pub visible: bool, invisible: bool, }
}

fn main() {
    let foo::Foo {} = foo::Foo::default();
    //~^ ERROR pattern does not mention field `visible` and inaccessible fields
}


