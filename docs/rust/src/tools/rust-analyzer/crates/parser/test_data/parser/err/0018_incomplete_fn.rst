src/tools/rust-analyzer/crates/parser/test_data/parser/err/0018_incomplete_fn.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl FnScopes {
    fn new_scope(&) -> ScopeId {
        let res = self.scopes.len();
        self.scopes.push(ScopeData { parent: None, entries: vec![] })
    }

    fn set_parent
}


