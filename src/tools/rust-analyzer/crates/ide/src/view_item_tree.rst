src/tools/rust-analyzer/crates/ide/src/view_item_tree.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use hir::db::DefDatabase;
use ide_db::base_db::FileId;
use ide_db::RootDatabase;

// Feature: Debug ItemTree
//
// Displays the ItemTree of the currently open file, for debugging.
//
// |===
// | Editor  | Action Name
//
// | VS Code | **rust-analyzer: Debug ItemTree**
// |===
pub(crate) fn view_item_tree(db: &RootDatabase, file_id: FileId) -> String {
    db.file_item_tree(file_id.into()).pretty_print()
}


