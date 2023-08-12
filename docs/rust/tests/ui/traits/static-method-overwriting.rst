tests/ui/traits/static-method-overwriting.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
mod base {
    pub trait HasNew {
        fn new() -> Self;
    }

    pub struct Foo {
        dummy: (),
    }

    impl ::base::HasNew for Foo {
        fn new() -> Foo {
            println!("Foo");
            Foo { dummy: () }
        }
    }

    pub struct Bar {
        dummy: (),
    }

    impl ::base::HasNew for Bar {
        fn new() -> Bar {
            println!("Bar");
            Bar { dummy: () }
        }
    }
}

pub fn main() {
    let _f: base::Foo = base::HasNew::new();
    let _b: base::Bar = base::HasNew::new();
}


