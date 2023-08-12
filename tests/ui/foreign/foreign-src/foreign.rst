tests/ui/foreign/foreign-src/foreign.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass



pub fn main() {
    libc.puts(rustrt.str_buf("hello, extern world 1"));
    libc.puts(rustrt.str_buf("hello, extern world 2"));
    libc.puts(rustrt.str_buf("hello, extern world 3"));
}


