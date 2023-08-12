src/tools/rustfmt/tests/source/long-match-arms-brace-newline.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_strings: true
// rustfmt-max_width: 80
// rustfmt-control_brace_style: AlwaysNextLine

fn main() {
    match x {
        aaaaaaaa::Bbbbb::Ccccccccccccc(_, Some(ref x)) if x ==
            "aaaaaaaaaaa \
            aaaaaaa \
            aaaaaa" => {
            Ok(())
        }
            _ => Err(x),
    }
}


