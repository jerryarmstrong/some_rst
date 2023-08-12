src/tools/rustfmt/tests/target/configs/match_arm_blocks/true.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-match_arm_blocks: true
// Wrap match-arms

fn main() {
    match lorem {
        true => {
            foooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(x)
        }
        false => {
            println!("{}", sit)
        }
    }
}


