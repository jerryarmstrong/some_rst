tests/ui/windows-subsystem-invalid.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: invalid windows subsystem `wrong`, only `windows` and `console` are allowed

#![windows_subsystem = "wrong"]

fn main() {}


