tests/ui/unpretty/avoid-crash.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test "error `.*`" -> "$$ERROR_MESSAGE"
// compile-flags: -o/tmp/ -Zunpretty=ast-tree

fn main() {}


