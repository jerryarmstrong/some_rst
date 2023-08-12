tests/ui/enum/suggest-default-attribute.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum Test { //~ HELP consider adding a derive
    #[default]
    //~^ ERROR cannot find attribute `default` in this scope
    First,
    Second,
}

fn main() {}


