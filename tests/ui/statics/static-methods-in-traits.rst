tests/ui/statics/static-methods-in-traits.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

mod a {
    pub trait Foo {
        fn foo() -> Self;
    }

    impl Foo for isize {
        fn foo() -> isize {
            3
        }
    }

    impl Foo for usize {
        fn foo() -> usize {
            5
        }
    }
}

pub fn main() {
    let x: isize = a::Foo::foo();
    let y: usize = a::Foo::foo();
    assert_eq!(x, 3);
    assert_eq!(y, 5);
}


