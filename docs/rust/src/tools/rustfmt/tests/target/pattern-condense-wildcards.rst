src/tools/rustfmt/tests/target/pattern-condense-wildcards.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true
// rustfmt-condense_wildcard_suffixes: true

fn main() {
    match x {
        Butt(..) => "hah",
        Tup(_) => "nah",
        Quad(_, _, x, _) => " also no rewrite",
        Quad(x, ..) => "condense me pls",
        Weird(x, _, _, /* don't condense before */ ..) => "pls work",
    }
}


