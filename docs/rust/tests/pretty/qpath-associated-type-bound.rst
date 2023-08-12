tests/pretty/qpath-associated-type-bound.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact


mod m {
    pub trait Tr {
        type Ts: super::Tu;
    }
}

trait Tu {
    fn dummy() {}
}

fn foo<T: m::Tr>() { <T as m::Tr>::Ts::dummy(); }

fn main() {}


