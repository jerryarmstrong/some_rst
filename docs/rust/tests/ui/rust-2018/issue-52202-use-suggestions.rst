tests/ui/rust-2018/issue-52202-use-suggestions.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// The local `use` suggestion should start with `crate::` (but the
// standard-library suggestions should not, obviously).

mod plumbing {
    pub struct Drain;
}

fn main() {
    let _d = Drain {};
    //~^ ERROR cannot find struct, variant or union type `Drain` in this scope
}


