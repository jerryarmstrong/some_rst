tests/ui/traits/impl-implicit-trait.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

// pretty-expanded FIXME #23616

enum option_<T> {
    none_,
    some_(T),
}

impl<T> option_<T> {
    pub fn foo(&self) -> bool { true }
}

enum option__ {
    none__,
    some__(isize)
}

impl option__ {
    pub fn foo(&self) -> bool { true }
}

pub fn main() {
}


