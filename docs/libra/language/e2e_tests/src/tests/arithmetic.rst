language/e2e_tests/src/tests/arithmetic.rs
==========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::compile_and_execute;

#[test]
fn simple_main() {
    let program = String::from(
        "
        main() {
            return;
        }
        ",
    );

    assert!(compile_and_execute(&program, vec![]).is_ok());
}

#[test]
fn simple_arithmetic() {
    let program = String::from(
        "
        main() {
            let a: u64;
            let b: u64;
            a = 2 + 3;
            assert(copy(a) == 5, 42);
            b = copy(a) - 1;
            assert(copy(b) == 4, 42);
            return;
        }
        ",
    );

    assert!(compile_and_execute(&program, vec![]).is_ok());
}


