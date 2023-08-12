tests/ui/sized/coinductive-2.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct Node<C: CollectionFactory<Self>> {
    _children: C::Collection,
}

trait CollectionFactory<T> {
    type Collection;
}

impl<T> CollectionFactory<T> for Vec<()> {
    type Collection = Vec<T>;
}

trait Collection<T>: Sized {
    fn push(&mut self, v: T);
}

impl<T> Collection<T> for Vec<T> {
    fn push(&mut self, v: T) {
        self.push(v)
    }
}

fn main() {
    let _ = Node::<Vec<()>> {
        _children: Vec::new(),
    };
}


