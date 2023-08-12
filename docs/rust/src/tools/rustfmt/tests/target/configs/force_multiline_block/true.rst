src/tools/rustfmt/tests/target/configs/force_multiline_block/true.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-force_multiline_blocks: true
// Option forces multiline match arm and closure bodies to be wrapped in a block

fn main() {
    match lorem {
        Lorem::Ipsum => {
            if ipsum {
                println!("dolor");
            }
        }
        Lorem::Dolor => println!("amet"),
    }
}

fn main() {
    result.and_then(|maybe_value| {
        match maybe_value {
            None => Err("oops"),
            Some(value) => Ok(1),
        }
    });
}


