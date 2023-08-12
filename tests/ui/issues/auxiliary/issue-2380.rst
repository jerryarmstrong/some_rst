tests/ui/issues/auxiliary/issue-2380.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="a"]
#![crate_type = "lib"]

pub trait i<T>
{
    fn dummy(&self, t: T) -> T { panic!() }
}

pub fn f<T>() -> Box<i<T>+'static> {
    impl<T> i<T> for () { }

    Box::new(()) as Box<i<T>+'static>
}


