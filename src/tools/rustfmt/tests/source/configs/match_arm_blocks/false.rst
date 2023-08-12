src/tools/rustfmt/tests/source/configs/match_arm_blocks/false.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-match_arm_blocks: false
// Wrap match-arms

fn main() {
    match lorem {
        true => foooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo(x),
        false => {
            println!("{}", sit)
        }
    }
}


