tests/ui/self/explicit-self-generic.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

#[derive(Copy, Clone)]
struct LM { resize_at: usize, size: usize }

enum HashMap<K,V> {
    HashMap_(LM, Vec<(K,V)>)
}

fn linear_map<K,V>() -> HashMap<K,V> {
    HashMap::HashMap_(LM{
        resize_at: 32,
        size: 0}, Vec::new())
}

impl<K,V> HashMap<K,V> {
    pub fn len(&mut self) -> usize {
        match *self {
            HashMap::HashMap_(ref l, _) => l.size
        }
    }
}

pub fn main() {
    let mut m: Box<_> = Box::new(linear_map::<(),()>());
    assert_eq!(m.len(), 0);
}


