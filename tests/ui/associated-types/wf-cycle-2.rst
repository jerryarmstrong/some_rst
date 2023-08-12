tests/ui/associated-types/wf-cycle-2.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait IntoIt {
    type Item;
}

impl<I> IntoIt for I {
    type Item = ();
}

trait BaseGraph
where
    <Self::VertexIter as IntoIt>::Item: Sized,
{
    type VertexIter: IntoIt;
}

fn main() {}


