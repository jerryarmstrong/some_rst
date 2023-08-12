tests/ui/parser/recover-struct.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    struct Test {
        Very
        Bad //~ ERROR found `Bad`
        Stuff
    }
}


