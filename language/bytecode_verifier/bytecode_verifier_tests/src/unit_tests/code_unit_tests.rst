language/bytecode_verifier/bytecode_verifier_tests/src/unit_tests/code_unit_tests.rs
====================================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use solana_libra_bytecode_verifier::CodeUnitVerifier;
use solana_libra_types::vm_error::StatusCode;
use solana_libra_vm::file_format::{self, Bytecode};

#[test]
fn invalid_fallthrough_br_true() {
    let module = file_format::dummy_procedure_module(vec![Bytecode::LdFalse, Bytecode::BrTrue(1)]);
    let errors = CodeUnitVerifier::verify(&module);
    assert_eq!(errors[0].major_status, StatusCode::INVALID_FALL_THROUGH);
}

#[test]
fn invalid_fallthrough_br_false() {
    let module = file_format::dummy_procedure_module(vec![Bytecode::LdTrue, Bytecode::BrFalse(1)]);
    let errors = CodeUnitVerifier::verify(&module);
    assert_eq!(errors[0].major_status, StatusCode::INVALID_FALL_THROUGH);
}

// all non-branch instructions should trigger invalid fallthrough; just check one of them
#[test]
fn invalid_fallthrough_non_branch() {
    let module = file_format::dummy_procedure_module(vec![Bytecode::LdTrue, Bytecode::Pop]);
    let errors = CodeUnitVerifier::verify(&module);
    assert_eq!(errors[0].major_status, StatusCode::INVALID_FALL_THROUGH);
}

#[test]
fn valid_fallthrough_branch() {
    let module = file_format::dummy_procedure_module(vec![Bytecode::Branch(0)]);
    let errors = CodeUnitVerifier::verify(&module);
    assert!(errors.is_empty());
}

#[test]
fn valid_fallthrough_ret() {
    let module = file_format::dummy_procedure_module(vec![Bytecode::Ret]);
    let errors = CodeUnitVerifier::verify(&module);
    assert!(errors.is_empty());
}

#[test]
fn valid_fallthrough_abort() {
    let module = file_format::dummy_procedure_module(vec![Bytecode::LdConst(7), Bytecode::Abort]);
    let errors = CodeUnitVerifier::verify(&module);
    assert!(errors.is_empty());
}


