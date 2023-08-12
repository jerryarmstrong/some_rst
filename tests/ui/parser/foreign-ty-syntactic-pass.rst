tests/ui/parser/foreign-ty-syntactic-pass.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {}

#[cfg(FALSE)]
extern "C" {
    type A: Ord;
    type A<'a> where 'a: 'static;
    type A<T: Ord> where T: 'static;
    type A = u8;
    type A<'a: 'static, T: Ord + 'static>: Eq + PartialEq where T: 'static + Copy = Vec<u8>;
}


