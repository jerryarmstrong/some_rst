src/tools/rustfmt/tests/target/issue-4577.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let s: String = "ABAABBAA"
        .chars()
        .filter(|c| if *c == 'A' { true } else { false })
        .map(|c| -> char {
            if c == 'A' {
                '0'
            } else {
                '1'
            }
        })
        .collect();

    println!("{}", s);
}


