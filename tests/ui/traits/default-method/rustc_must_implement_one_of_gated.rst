tests/ui/traits/default-method/rustc_must_implement_one_of_gated.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[rustc_must_implement_one_of(eq, neq)]
//~^ the `#[rustc_must_implement_one_of]` attribute is used to change minimal complete definition of a trait, it's currently in experimental form and should be changed before being exposed outside of the std
trait Equal {
    fn eq(&self, other: &Self) -> bool {
        !self.neq(other)
    }

    fn neq(&self, other: &Self) -> bool {
        !self.eq(other)
    }
}

fn main() {}


