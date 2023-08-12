tests/ui/structs-enums/struct-literal-dtor.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

struct foo {
    x: String,
}

impl Drop for foo {
    fn drop(&mut self) {
        println!("{}", self.x);
    }
}

pub fn main() {
    let _z = foo {
        x: "Hello".to_string()
    };
}


