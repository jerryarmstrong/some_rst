src/tools/clippy/tests/ui/wild_in_or_pats.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::wildcard_in_or_patterns)]

fn main() {
    match "foo" {
        "a" => {
            dbg!("matched a");
        },
        "bar" | _ => {
            dbg!("matched (bar or) wild");
        },
    };
    match "foo" {
        "a" => {
            dbg!("matched a");
        },
        "bar" | "bar2" | _ => {
            dbg!("matched (bar or bar2 or) wild");
        },
    };
    match "foo" {
        "a" => {
            dbg!("matched a");
        },
        _ | "bar" | _ => {
            dbg!("matched (bar or) wild");
        },
    };
    match "foo" {
        "a" => {
            dbg!("matched a");
        },
        _ | "bar" => {
            dbg!("matched (bar or) wild");
        },
    };
}


