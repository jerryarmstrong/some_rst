tests/ui/traits/mutual-recursion-issue-75860.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn iso<A, B, F1, F2>(a: F1, b: F2) -> (Box<dyn Fn(A) -> B>, Box<dyn Fn(B) -> A>)
    where
        F1: (Fn(A) -> B) + 'static,
        F2: (Fn(B) -> A) + 'static,
{
    (Box::new(a), Box::new(b))
}
pub fn iso_un_option<A, B>() -> (Box<dyn Fn(A) -> B>, Box<dyn Fn(B) -> A>) {
   let left = |o_a: Option<_>| o_a.unwrap();
    let right = |o_b: Option<_>| o_b.unwrap();
    iso(left, right)
    //~^ ERROR overflow
}

fn main() {}


