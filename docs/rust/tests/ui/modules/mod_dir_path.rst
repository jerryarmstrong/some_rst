tests/ui/modules/mod_dir_path.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_macros)]
// ignore-pretty issue #37195

mod mod_dir_simple {
    #[path = "test.rs"]
    pub mod syrup;
}

pub fn main() {
    assert_eq!(mod_dir_simple::syrup::foo(), 10);

    #[path = "auxiliary"]
    mod foo {
        mod two_macros_2;
    }

    #[path = "auxiliary"]
    mod bar {
        macro_rules! m { () => { mod two_macros_2; } }
        m!();
    }
}


