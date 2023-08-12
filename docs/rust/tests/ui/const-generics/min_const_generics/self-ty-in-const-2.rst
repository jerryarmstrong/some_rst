tests/ui/const-generics/min_const_generics/self-ty-in-const-2.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Bar<T>(T);

trait Baz {
    fn hey();
}

impl Baz for u16 {
    fn hey() {
        let _: [u8; std::mem::size_of::<Self>()]; // ok
    }
}

impl<T> Baz for Bar<T> {
    fn hey() {
        let _: [u8; std::mem::size_of::<Self>()]; //~ERROR generic `Self`
    }
}

fn main() {}


