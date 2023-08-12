tests/ui/sized/coinductive-1.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
struct Node<C: Trait<Self>>(C::Assoc);

trait Trait<T> {
    type Assoc;
}

impl<T> Trait<T> for Vec<()> {
    type Assoc = Vec<T>;
}

fn main() {
    let _ = Node::<Vec<()>>(Vec::new());
}


