tests/ui/impl-not-adjacent-to-type.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

mod foo {
    pub struct Point {
        pub x: i32,
        pub y: i32,
    }
}

impl foo::Point {
    fn x(&self) -> i32 { self.x }
}

fn main() {
    assert_eq!((foo::Point { x: 1, y: 3}).x(), 1);
}


