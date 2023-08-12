src/tools/rustfmt/tests/source/configs/control_brace_style/always_next_line.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-control_brace_style: AlwaysNextLine
// Control brace style

fn main() {
    if lorem { println!("ipsum!"); } else { println!("dolor!"); }
    match magi {
        Homura => "Akemi",
        Madoka => "Kaname",
    }
}


