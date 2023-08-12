tests/ui/associated-type-bounds/associated-item-through-where-clause.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Foo {
    type Item;
}

trait Bar
where
    Self: Foo,
{
}

#[allow(dead_code)]
fn foo<M>(_m: M)
where
    M: Bar,
    M::Item: Send,
{
}

fn main() {}


