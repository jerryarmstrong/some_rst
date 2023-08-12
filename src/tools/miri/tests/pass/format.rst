src/tools/miri/tests/pass/format.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!("Hello {}", 13);
    println!("{:0<width$}", "hello", width = 10);
}


