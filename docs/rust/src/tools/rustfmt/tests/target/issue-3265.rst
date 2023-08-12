src/tools/rustfmt/tests/target/issue-3265.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-newline_style: Windows
#[cfg(test)]
mod test {
    summary_test! {
        tokenize_recipe_interpolation_eol,
    "foo: # some comment
 {{hello}}
",
    "foo: \
    {{hello}} \
    {{ahah}}",
        "N:#$>^{N}$<.",
      }
}


