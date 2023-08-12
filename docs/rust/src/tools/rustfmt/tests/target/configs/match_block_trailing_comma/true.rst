src/tools/rustfmt/tests/target/configs/match_block_trailing_comma/true.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-match_block_trailing_comma: true
// Match block trailing comma

fn main() {
    match lorem {
        Lorem::Ipsum => {
            println!("ipsum");
        },
        Lorem::Dolor => println!("dolor"),
    }
}


