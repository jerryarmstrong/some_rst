tests/ui/unresolved/unresolved-candidates.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
    pub trait Trait {}
}

mod b {
    use Trait; //~ ERROR unresolved import `Trait`
}

mod c {
    impl Trait for () {} //~ ERROR cannot find trait `Trait` in this scope
}

fn main() {}


