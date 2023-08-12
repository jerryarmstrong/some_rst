language/e2e_tests/src/tests/pack_unpack.rs
===========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::compile_and_execute;

#[test]
fn simple_unpack() {
    let program = String::from(
        "
modules:
module Test {
    resource T { i: u64, b: bool }

    public new_t(): Self.T {
        return T { i: 0, b: false };
    }

    public unpack_t(t: Self.T) {
        let i: u64;
        let flag: bool;
        T { i, b: flag } = move(t);
        return;
    }

}
script:
import 0x0.Test;
main() {
    let t: Test.T;

    t = Test.new_t();
    Test.unpack_t(move(t));

    return;
}",
    );
    assert!(compile_and_execute(&program, vec![]).is_ok());
}


