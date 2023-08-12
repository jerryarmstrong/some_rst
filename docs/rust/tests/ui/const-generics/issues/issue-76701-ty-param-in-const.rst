tests/ui/const-generics/issues/issue-76701-ty-param-in-const.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn ty_param<T>() -> [u8; std::mem::size_of::<T>()] {
    //~^ ERROR generic parameters may not be used in const operations
    todo!()
}

fn const_param<const N: usize>() -> [u8; N + 1] {
    //~^ ERROR generic parameters may not be used in const operations
    todo!()
}

fn main() {}


