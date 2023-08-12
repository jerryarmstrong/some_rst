tests/ui/lint/dead-code/empty-unused-enum.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused)]

enum E {} //~ ERROR enum `E` is never used

fn main() {}


