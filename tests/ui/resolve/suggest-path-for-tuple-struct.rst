tests/ui/resolve/suggest-path-for-tuple-struct.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod module {
    pub struct SomeTupleStruct(u8);
    pub struct SomeRegularStruct {
        foo: u8
    }

    impl SomeTupleStruct {
        pub fn new() -> Self {
            Self(0)
        }
    }
    impl SomeRegularStruct {
        pub fn new() -> Self {
            Self { foo: 0 }
        }
    }
}

use module::{SomeTupleStruct, SomeRegularStruct};

fn main() {
    let _ = SomeTupleStruct.new();
    //~^ ERROR expected value, found struct `SomeTupleStruct`
    let _ = SomeRegularStruct.new();
    //~^ ERROR expected value, found struct `SomeRegularStruct`
}


