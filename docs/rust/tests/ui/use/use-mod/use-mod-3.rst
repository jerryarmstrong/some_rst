tests/ui/use/use-mod/use-mod-3.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use foo::bar::{ //~ ERROR module `bar` is private
    self
};
use foo::bar::{ //~ ERROR module `bar` is private
    Bar
};

mod foo {
    mod bar { pub type Bar = isize; }
}

fn main() {}


