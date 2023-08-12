src/tools/clippy/tests/ui/auxiliary/wildcard_imports_helper.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub use crate::extern_exports::*;

pub fn extern_foo() {}
pub fn extern_bar() {}

pub struct ExternA;

pub mod inner {
    pub mod inner_for_self_import {
        pub fn inner_extern_foo() {}
        pub fn inner_extern_bar() {}
    }
}

mod extern_exports {
    pub fn extern_exported() {}
    pub struct ExternExportedStruct;
    pub enum ExternExportedEnum {
        A,
    }
}

pub mod prelude {
    pub mod v1 {
        pub struct PreludeModAnywhere;
    }
}


