src/tools/rust-analyzer/crates/proc-macro-srv/src/abis/abi_sysroot/ra_server/symbol.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Symbol interner for proc-macro-srv

use std::{cell::RefCell, collections::HashMap};
use tt::SmolStr;

thread_local! {
    static SYMBOL_INTERNER: RefCell<SymbolInterner> = Default::default();
}

// ID for an interned symbol.
#[derive(Hash, Eq, PartialEq, Copy, Clone)]
pub struct Symbol(u32);

impl Symbol {
    pub fn intern(data: &str) -> Symbol {
        SYMBOL_INTERNER.with(|i| i.borrow_mut().intern(data))
    }

    pub fn text(&self) -> SmolStr {
        SYMBOL_INTERNER.with(|i| i.borrow().get(self).clone())
    }
}

#[derive(Default)]
struct SymbolInterner {
    idents: HashMap<SmolStr, u32>,
    ident_data: Vec<SmolStr>,
}

impl SymbolInterner {
    fn intern(&mut self, data: &str) -> Symbol {
        if let Some(index) = self.idents.get(data) {
            return Symbol(*index);
        }

        let index = self.idents.len() as u32;
        let data = SmolStr::from(data);
        self.ident_data.push(data.clone());
        self.idents.insert(data, index);
        Symbol(index)
    }

    fn get(&self, sym: &Symbol) -> &SmolStr {
        &self.ident_data[sym.0 as usize]
    }
}


