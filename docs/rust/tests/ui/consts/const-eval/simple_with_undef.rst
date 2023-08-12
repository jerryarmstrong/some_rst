tests/ui/consts/const-eval/simple_with_undef.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

const PARSE_BOOL: Option<&'static str> = None;
static FOO: (Option<&str>, u32) = (PARSE_BOOL, 42);

fn main() {}


