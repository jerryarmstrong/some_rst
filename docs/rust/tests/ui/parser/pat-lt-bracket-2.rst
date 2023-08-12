tests/ui/parser/pat-lt-bracket-2.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a(B<) {}
   //~^ error: expected one of `:`, `@`, or `|`, found `<`

fn main() {}


