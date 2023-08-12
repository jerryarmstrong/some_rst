src/tools/rustfmt/tests/target/issue-2930.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Visual
fn main() {
    let (first_variable, second_variable) = (this_is_something_with_an_extraordinarily_long_name,
                                             this_variable_name_is_also_pretty_long);
}


