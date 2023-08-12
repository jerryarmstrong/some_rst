src/tools/rustfmt/tests/target/match_overflow_expr.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-overflow_delimited_expr: true

fn main() {
    println!("Foobar: {}", match "input" {
        "a" => "",
        "b" => "",
        "c" => "",
        "d" => "",
        "e" => "",
        "f" => "",
        "g" => "",
        "h" => "",
        "i" => "",
        "j" => "",
        "k" => "",
        "l" => "",
        "m" => "",
        "n" => "",
        "o" => "",
        "p" => "",
        "q" => "",
        "r" => "Rust",
    });
}

fn main() {
    println!(
        "Very Long Input String Which Makes It Impossible To Fit On The Same Line: {}",
        match "input" {
            "a" => "",
            "b" => "",
            "c" => "",
            "d" => "",
            "e" => "",
            "f" => "",
            "g" => "",
            "h" => "",
            "i" => "",
            "j" => "",
            "k" => "",
            "l" => "",
            "m" => "",
            "n" => "",
            "o" => "",
            "p" => "",
            "q" => "",
            "r" => "Rust",
        }
    );
}


