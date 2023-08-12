tests/ui/match/match-wildcards.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:squirrelcupcake
// ignore-emscripten no processes

fn cmp() -> isize {
    match (Some('a'), None::<char>) {
        (Some(_), _) => {
            panic!("squirrelcupcake");
        }
        (_, Some(_)) => {
            panic!();
        }
        _ => {
            panic!("wat");
        }
    }
}

fn main() {
    println!("{}", cmp());
}


