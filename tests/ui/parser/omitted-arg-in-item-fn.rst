tests/ui/parser/omitted-arg-in-item-fn.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x) { //~ ERROR expected one of `:`, `@`, or `|`, found `)`
}

fn main() {}


