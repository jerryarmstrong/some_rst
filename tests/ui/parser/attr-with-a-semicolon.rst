tests/ui/parser/attr-with-a-semicolon.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Debug, Clone)]; //~ERROR expected item after attributes
struct Foo;

fn main() {}


