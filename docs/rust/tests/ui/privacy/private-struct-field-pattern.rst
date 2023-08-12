tests/ui/privacy/private-struct-field-pattern.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use a::Foo;

mod a {
    pub struct Foo {
        x: isize
    }

    pub fn make() -> Foo {
        Foo { x: 3 }
    }
}

fn main() {
    match a::make() {
        Foo { x: _ } => {}  //~ ERROR field `x` of struct `Foo` is private
    }
}


