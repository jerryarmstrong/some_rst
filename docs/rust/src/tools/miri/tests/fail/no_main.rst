src/tools/miri/tests/fail/no_main.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@error-pattern: miri can only run programs that have a main function
#![no_main]


