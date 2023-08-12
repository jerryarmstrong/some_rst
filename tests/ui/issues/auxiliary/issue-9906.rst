tests/ui/issues/auxiliary/issue-9906.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub use other::FooBar;
pub use other::foo;

mod other {
    pub struct FooBar{value: isize}
    impl FooBar{
        pub fn new(val: isize) -> FooBar {
            FooBar{value: val}
        }
    }

    pub fn foo(){
        1+1;
    }
}


