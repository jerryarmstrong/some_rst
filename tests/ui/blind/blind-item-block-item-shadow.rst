tests/ui/blind/blind-item-block-item-shadow.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo { pub struct Bar; }

fn main() {
    {
        struct Bar;
        use foo::Bar;
        //~^ ERROR the name `Bar` is defined multiple times
    }
}


