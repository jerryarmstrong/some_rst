tests/ui/async-await/issue-54239-private-type-triggers-lint.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #54239, shouldn't trigger lint.
// check-pass
// edition:2018

#![deny(missing_debug_implementations)]

struct DontLookAtMe(i32);

async fn secret() -> DontLookAtMe {
    DontLookAtMe(41)
}

pub async fn looking() -> i32 { // Shouldn't trigger lint here.
    secret().await.0
}

fn main() {}


