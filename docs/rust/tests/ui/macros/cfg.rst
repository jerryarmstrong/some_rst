tests/ui/macros/cfg.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    cfg!(); //~ ERROR macro requires a cfg-pattern
    cfg!(123); //~ ERROR expected identifier
    cfg!(foo = 123); //~ ERROR literal in `cfg` predicate value must be a string
    cfg!(foo, bar); //~ ERROR expected 1 cfg-pattern
}


