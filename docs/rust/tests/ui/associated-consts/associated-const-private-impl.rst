tests/ui/associated-consts/associated-const-private-impl.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod bar1 {
    pub use self::bar2::Foo;
    mod bar2 {
        pub struct Foo;

        impl Foo {
            const ID: i32 = 1;
        }
    }
}

fn main() {
    assert_eq!(1, bar1::Foo::ID);
    //~^ERROR associated constant `ID` is private
}


