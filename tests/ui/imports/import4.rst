tests/ui/imports/import4.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: import


mod a { pub use b::foo; }
mod b { pub use a::foo; }

fn main() { println!("loop"); }


