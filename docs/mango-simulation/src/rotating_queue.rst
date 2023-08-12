src/rotating_queue.rs
=====================

Last edited: 2023-05-15 14:19:21

Contents:

.. code-block:: rs

    use std::{
    collections::VecDeque,
    sync::{Arc, RwLock},
};

pub struct RotatingQueue<T> {
    deque: Arc<RwLock<VecDeque<T>>>,
}

impl<T: Clone> RotatingQueue<T> {
    pub fn new<F>(size: usize, creator_functor: F) -> Self
    where
        F: Fn() -> T,
    {
        let item = Self {
            deque: Arc::new(RwLock::new(VecDeque::<T>::new())),
        };
        {
            let mut deque = item.deque.write().unwrap();
            for _i in 0..size {
                deque.push_back(creator_functor());
            }
        }
        item
    }

    pub fn get(&self) -> T {
        let mut deque = self.deque.write().unwrap();
        let current = deque.pop_front().unwrap();
        deque.push_back(current.clone());
        current
    }
}


