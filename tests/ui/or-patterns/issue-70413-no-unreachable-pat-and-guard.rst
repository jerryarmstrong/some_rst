tests/ui/or-patterns/issue-70413-no-unreachable-pat-and-guard.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(unreachable_patterns)]

fn main() {
    match (3,42) {
        (a,_) | (_,a) if a > 10 => {println!("{}", a)}
        _ => ()
    }

    match Some((3,42)) {
        Some((a, _)) | Some((_, a)) if a > 10 => {println!("{}", a)}
        _ => ()

    }

    match Some((3,42)) {
        Some((a, _) | (_, a)) if a > 10 => {println!("{}", a)}
        _ => ()
    }
}


