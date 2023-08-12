tests/ui/privacy/private-field-ty-err.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = foo::Foo::default();
    if x.len {
        //~^ ERROR field `len` of struct `Foo` is private
        println!("foo");
    }
}

mod foo {
    #[derive(Default)]
    pub struct Foo {
        len: String,
    }

    impl Foo {
        pub fn len(&self) -> usize {
            42
        }
    }
}


