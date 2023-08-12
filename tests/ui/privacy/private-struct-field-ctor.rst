tests/ui/privacy/private-struct-field-ctor.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
    pub struct Foo {
        x: isize
    }
}

fn main() {
    let s = a::Foo { x: 1 };    //~ ERROR field `x` of struct `Foo` is private
}


