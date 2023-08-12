tests/ui/codemap_tests/unicode.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: normal expanded
//[expanded] check-pass
//[expanded]compile-flags: -Zunpretty=expanded

extern "路濫狼á́́" fn foo() {} //[normal]~ ERROR invalid ABI

fn main() { }


