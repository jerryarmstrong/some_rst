tests/ui/privacy/private-in-public-lint.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod m1 {
    pub struct Pub;
    struct Priv;

    impl Pub {
        pub fn f() -> Priv {Priv} //~ ERROR private type `m1::Priv` in public interface
    }
}

mod m2 {
    pub struct Pub;
    struct Priv;

    impl Pub {
        pub fn f() -> Priv {Priv} //~ ERROR private type `m2::Priv` in public interface
    }
}

fn main() {}


