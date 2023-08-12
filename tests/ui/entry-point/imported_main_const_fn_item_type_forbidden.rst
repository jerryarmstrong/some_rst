tests/ui/entry-point/imported_main_const_fn_item_type_forbidden.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(imported_main)]
#![feature(type_alias_impl_trait)]
#![allow(incomplete_features)]
pub mod foo {
    type MainFn = impl Fn();

    fn bar() {}
    pub const BAR: MainFn = bar;
}

use foo::BAR as main; //~ ERROR `main` function not found in crate


