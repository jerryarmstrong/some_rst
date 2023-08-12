tests/ui/rfc-2497-if-let-chains/then-else-blocks.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(if_let_guard, let_chains)]

fn check_if_let(opt: Option<Option<Option<i32>>>, value: i32) -> bool {
    if let Some(first) = opt
        && let Some(second) = first
        && let Some(third) = second
        && third == value
    {
        true
    }
    else {
        false
    }
}

fn check_let_guard(opt: Option<Option<Option<i32>>>, value: i32) -> bool {
    match opt {
        Some(first) if let Some(second) = first && let Some(third) = second && third == value => {
            true
        }
        _ => {
            false
        }
    }
}

fn check_while_let(opt: Option<Option<Option<i32>>>, value: i32) -> bool {
    while let Some(first) = opt
        && let Some(second) = first
        && let Some(third) = second
        && third == value
    {
        return true;
    }
    false
}

fn main() {
    assert_eq!(check_if_let(Some(Some(Some(1))), 1), true);
    assert_eq!(check_if_let(Some(Some(Some(1))), 9), false);

    assert_eq!(check_let_guard(Some(Some(Some(1))), 1), true);
    assert_eq!(check_let_guard(Some(Some(Some(1))), 9), false);

    assert_eq!(check_while_let(Some(Some(Some(1))), 1), true);
    assert_eq!(check_while_let(Some(Some(Some(1))), 9), false);
}


