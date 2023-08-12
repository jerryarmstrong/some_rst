src/tools/rustfmt/tests/source/issue-3636.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-file_lines: [{"file":"tests/source/issue-3636.rs","range":[4,7]},{"file":"tests/target/issue-3636.rs","range":[3,6]}]

fn foo() {
    let x =
        42;
    let y =
        42;
    let z = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    let z = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb";   
}


