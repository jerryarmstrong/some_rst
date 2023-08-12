tests/ui/use/use-mod/use-mod-5.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    pub mod bar {
        pub fn drop() {}
    }
}

use foo::bar::self;
//~^ ERROR `self` imports are only allowed within a { } list

fn main() {
    // Because of error recovery this shouldn't error
    bar::drop();
}


