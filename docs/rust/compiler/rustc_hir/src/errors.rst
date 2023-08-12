compiler/rustc_hir/src/errors.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::LangItem;

#[derive(Debug, Copy, Clone, PartialEq, Eq, Hash, Encodable, Decodable)]
pub struct LangItemError(pub LangItem);

impl ToString for LangItemError {
    fn to_string(&self) -> String {
        format!("requires `{}` lang_item", self.0.name())
    }
}


