src/tools/rustfmt/tests/target/format_strings/issue-2833.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_strings: true
// rustfmt-max_width: 80

fn test1() {
    let expected = "\
but Doctor Watson has to have it taken out for him and dusted,
";
}

fn test2() {
    let expected = "\
[Omitted long matching line]
but Doctor Watson has to have it taken out for him and dusted,
";
}


