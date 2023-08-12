compiler/rustc_hir/src/weak_lang_items.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Validity checking for weak lang items

use crate::LangItem;

use rustc_span::symbol::{sym, Symbol};

macro_rules! weak_lang_items {
    ($($item:ident, $sym:ident;)*) => {
        pub static WEAK_LANG_ITEMS: &[LangItem] = &[$(LangItem::$item,)*];

        impl LangItem {
            pub fn is_weak(self) -> bool {
                matches!(self, $(LangItem::$item)|*)
            }

            pub fn link_name(self) -> Option<Symbol> {
                match self {
                    $( LangItem::$item => Some(sym::$sym),)*
                    _ => None,
                }
            }
        }
    }
}

weak_lang_items! {
    PanicImpl,          rust_begin_unwind;
    EhPersonality,      rust_eh_personality;
    EhCatchTypeinfo,    rust_eh_catch_typeinfo;
}


