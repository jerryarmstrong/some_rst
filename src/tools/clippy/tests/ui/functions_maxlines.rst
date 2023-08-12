src/tools/clippy/tests/ui/functions_maxlines.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::too_many_lines)]

fn good_lines() {
    /* println!("This is good."); */
    // println!("This is good.");
    /* */ // println!("This is good.");
    /* */ // println!("This is good.");
    /* */ // println!("This is good.");
    /* */ // println!("This is good.");
    /* println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good."); */
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
    println!("This is good.");
}

fn bad_lines() {
    println!("Dont get confused by braces: {{}}");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
    println!("This is bad.");
}

fn main() {}


