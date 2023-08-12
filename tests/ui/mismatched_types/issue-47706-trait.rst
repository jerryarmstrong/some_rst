tests/ui/mismatched_types/issue-47706-trait.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T {
    fn f(&self, _: ()) {
        None::<()>.map(Self::f);
    }
    //~^^ ERROR function is expected to take a single 0-tuple as argument
}

fn main() {}


