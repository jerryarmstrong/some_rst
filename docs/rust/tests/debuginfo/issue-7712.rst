tests/debuginfo/issue-7712.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C debuginfo=1
// min-lldb-version: 310

pub trait TraitWithDefaultMethod : Sized {
    fn method(self) {
        ()
    }
}

struct MyStruct;

impl TraitWithDefaultMethod for MyStruct { }

pub fn main() {
    MyStruct.method();
}


