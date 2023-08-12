tests/ui/sized/coinductive-1-gat.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
struct Node<C: Trait>(C::Assoc::<Self>);

trait Trait {
    type Assoc<T>;
}

impl Trait for Vec<()> {
    type Assoc<T> = Vec<T>;
}

fn main() {
    let _ = Node::<Vec<()>>(Vec::new());
}


