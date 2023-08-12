tests/ui/rfc-2565-param-attrs/attr-without-param.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(FALSE)]
impl S {
    fn f(#[attr]) {} //~ ERROR expected parameter name, found `)`
}

#[cfg(FALSE)]
impl T for S {
    fn f(#[attr]) {} //~ ERROR expected parameter name, found `)`
}

#[cfg(FALSE)]
trait T {
    fn f(#[attr]); //~ ERROR expected argument name, found `)`
}

fn main() {}


