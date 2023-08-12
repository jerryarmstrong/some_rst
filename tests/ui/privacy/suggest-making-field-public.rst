tests/ui/privacy/suggest-making-field-public.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
mod a {
    pub struct A(pub(self)String);
}

mod b {
    use crate::a::A;
    pub fn x() {
        A("".into()); //~ ERROR cannot initialize a tuple struct which contains private fields
    }
}
fn main() {
    a::A("a".into()); //~ ERROR tuple struct constructor `A` is private
    b::x();
}


