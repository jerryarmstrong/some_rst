tests/ui/issues/issue-57399-self-return-impl-trait.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait T {
    type T;
}

impl T for i32 {
    type T = u32;
}

struct S<A> {
    a: A,
}


impl From<u32> for S<<i32 as T>::T> {
    fn from(a: u32) -> Self {
        Self { a }
    }
}

fn main() {}


