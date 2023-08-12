tests/ui/deriving/deriving-in-fn.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]

pub fn main() {
    #[derive(Debug)]
    struct Foo {
        foo: isize,
    }

    let f = Foo { foo: 10 };
    format!("{:?}", f);
}


