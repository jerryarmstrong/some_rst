tests/ui/issues/auxiliary/issue-34796-aux.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
pub trait Future {
    type Item;
    type Error;
}

impl Future for u32 {
    type Item = ();
    type Error = Box<()>;
}

fn foo() -> Box<Future<Item=(), Error=Box<()>>> {
    Box::new(0u32)
}

pub fn bar<F, A, B>(_s: F)
    where F: Fn(A) -> B,
{
    foo();
}


