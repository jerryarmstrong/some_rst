tests/incremental/issue-62649-path-collisions-happen.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: rpass1 rpass2

#[cfg(rpass1)]
pub trait Something {
    fn foo();
}

#[cfg(rpass2)]
pub struct Something {
    pub foo: u8,
}

fn main() {}


