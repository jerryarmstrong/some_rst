tests/ui/span/auxiliary/transitive_dep_two.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate transitive_dep_three;

transitive_dep_three::define_parse_error!();


