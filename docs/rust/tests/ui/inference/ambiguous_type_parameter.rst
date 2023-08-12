tests/ui/inference/ambiguous_type_parameter.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::collections::HashMap;

trait Store<K, V> {
    fn get_raw(&self, key: &K) -> Option<()>;
}

struct InMemoryStore;

impl<K> Store<String, HashMap<K, String>> for InMemoryStore {
    fn get_raw(&self, key: &String) -> Option<()> {
        None
    }
}

fn main() {
    InMemoryStore.get_raw(&String::default()); //~ ERROR type annotations needed
}


