language/tools/move-resource-viewer/src/module_cache.rs
=======================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use move_binary_format::CompiledModule;
use move_core_types::language_storage::ModuleId;
use std::{cell::RefCell, collections::hash_map::HashMap, hash::Hash, rc::Rc};

pub struct ModuleCacheImpl<K, V> {
    id_map: RefCell<HashMap<K, usize>>,
    modules: RefCell<Vec<Rc<V>>>,
}

impl<K, V> ModuleCacheImpl<K, V>
where
    K: Eq + Hash,
{
    pub fn new() -> Self {
        Self {
            id_map: RefCell::new(HashMap::new()),
            modules: RefCell::new(vec![]),
        }
    }

    pub fn insert(&self, key: K, module: V) -> Rc<V> {
        self.modules.borrow_mut().push(Rc::new(module));
        let idx = self.modules.borrow().len() - 1;
        self.id_map.borrow_mut().insert(key, idx);
        self.modules
            .borrow()
            .last()
            .expect("ModuleCache: last() after push() impossible failure")
            .clone()
    }

    pub fn get(&self, key: &K) -> Option<Rc<V>> {
        self.id_map
            .borrow()
            .get(key)
            .and_then(|idx| self.modules.borrow().get(*idx).cloned())
    }
}

pub type ModuleCache = ModuleCacheImpl<ModuleId, CompiledModule>;


