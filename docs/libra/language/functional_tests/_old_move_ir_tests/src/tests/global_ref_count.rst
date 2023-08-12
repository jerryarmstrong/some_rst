language/functional_tests/_old_move_ir_tests/src/tests/global_ref_count.rs
==========================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::*;
use move_ir::{assert_no_error, assert_other_error};

#[test]
fn increment_borrow_field() {
    let mut test_env = TestEnvironment::default();
    let sender = hex::encode(test_env.accounts.get_address(0));
    let program = format!(
        "
modules:
module Test {{
    resource T {{ i: u64 }}

    public test() {{
        let t;
        let t_ref;
        let i_ref;
        let sender;

        t = T {{ i: 0 }};
        move_to_sender<T>(move(t));

        sender = get_txn_sender();
        t_ref = borrow_global<T>(copy(sender));
        i_ref = &copy(t_ref).i;
        _ = move(t_ref);

        t_ref = borrow_global<T>(copy(sender));
        _ = move(t_ref);
        _ = move(i_ref);
    }}
}}
script:
import 0x{0}.Test;
main() {{
    Test.test();
    return;
}}",
        sender
    );
    assert_other_error!(test_env.run(to_script(program.as_bytes(), vec![])), format!("Invalid borrow of global resource 0x{0}.0x{0}.Test.T. There already exists a reference to this resource. You must free all references to this resource before calling \'borrow_global\' again.", sender))
}

#[test]
fn increment_copy() {
    let mut test_env = TestEnvironment::default();
    let sender = hex::encode(test_env.accounts.get_address(0));
    let program = format!(
        "
modules:
module Test {{
    resource T {{ i: u64 }}

    public test() {{
        let t;
        let t_ref;
        let i_ref;
        let sender;

        t = T {{ i: 0 }};
        move_to_sender<T>(move(t));

        sender = get_txn_sender();
        t_ref = borrow_global<T>(copy(sender));
        i_ref = copy(t_ref);
        _ = move(t_ref);

        t_ref = borrow_global<T>(copy(sender));
        _ = move(t_ref);
        _ = move(i_ref);
    }}
}}
script:
import 0x{0}.Test;
main() {{
    Test.test();
    return;
}}",
        sender
    );
    assert_other_error!(test_env.run(to_script(program.as_bytes(), vec![])),  format!("Invalid borrow of global resource 0x{0}.0x{0}.Test.T. There already exists a reference to this resource. You must free all references to this resource before calling \'borrow_global\' again.", sender))
}


