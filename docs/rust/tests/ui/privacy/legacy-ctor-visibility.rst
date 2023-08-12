tests/ui/privacy/legacy-ctor-visibility.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use m::S;

mod m {
    pub struct S(u8);

    mod n {
        use S;
        fn f() {
            S(10);
            //~^ ERROR expected function, tuple struct or tuple variant, found struct `S`
        }
    }
}

fn main() {}


