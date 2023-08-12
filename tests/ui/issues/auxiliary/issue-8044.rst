tests/ui/issues/auxiliary/issue-8044.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct BTree<V> {
    pub node: TreeItem<V>,
}

pub enum TreeItem<V> {
    TreeLeaf { value: V },
}

pub fn leaf<V>(value: V) -> TreeItem<V> {
    TreeItem::TreeLeaf { value: value }
}

fn main() {
    BTree::<isize> { node: leaf(1) };
}


