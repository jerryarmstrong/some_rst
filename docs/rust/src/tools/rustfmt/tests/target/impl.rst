src/tools/rustfmt/tests/target/impl.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test impls

impl<T> JSTraceable for SmallVec<[T; 1]> {}

impl<K, V, NodeRef: Deref<Target = Node<K, V>>> Handle<NodeRef, handle::Edge, handle::Internal> {
    // Keep this.
}

impl<V> Test<V>
where
    V: Clone, // This comment is NOT removed by formatting!
{
    pub fn new(value: V) -> Self {
        Test {
            cloned_value: value.clone(),
            value,
        }
    }
}

impl X<T> /* comment */ {}
impl Y<T> // comment
{
}

impl<T> Foo for T
// comment1
where
    // comment2
    // blah
    T: Clone,
{
}

// #1823
default impl Trait for X {}
default unsafe impl Trait for Y {}
pub default unsafe impl Trait for Z {}

// #2212
impl ConstWithDefault {
    default const CAN_RECONSTRUCT_QUERY_KEY: bool = false;
}


