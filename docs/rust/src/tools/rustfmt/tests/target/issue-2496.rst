src/tools/rustfmt/tests/target/issue-2496.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Visual
fn main() {
    match option {
        None => some_function(first_reasonably_long_argument,
                              second_reasonably_long_argument),
    }
}

fn main() {
    match option {
        None => some_function(first_reasonably_long_argument,
                              second_reasonably_long_argument),
    }
}


