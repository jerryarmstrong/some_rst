language/bytecode_verifier/bytecode_verifier_tests/src/unit_tests/negative_stack_size_tests.rs
==============================================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use solana_libra_bytecode_verifier::CodeUnitVerifier;
use solana_libra_types::vm_error::StatusCode;
use solana_libra_vm::file_format::{self, Bytecode};

#[test]
fn one_pop_no_push() {
    let module = file_format::dummy_procedure_module(vec![Bytecode::Pop, Bytecode::Ret]);
    let errors = CodeUnitVerifier::verify(&module);
    println!("{:?}", errors);
    assert_eq!(
        errors[0].major_status,
        StatusCode::NEGATIVE_STACK_SIZE_WITHIN_BLOCK
    );
}

#[test]
fn one_pop_one_push() {
    // Height: 0 + (-1 + 1) = 0 would have passed original usage verifier
    let module = file_format::dummy_procedure_module(vec![Bytecode::ReadRef, Bytecode::Ret]);
    let errors = CodeUnitVerifier::verify(&module);
    assert_eq!(
        errors[0].major_status,
        StatusCode::NEGATIVE_STACK_SIZE_WITHIN_BLOCK
    );
}

#[test]
fn two_pop_one_push() {
    // Height: 0 + 1 + (-2 + 1) = 0 would have passed original usage verifier
    let module = file_format::dummy_procedure_module(vec![
        Bytecode::LdConst(0),
        Bytecode::Add,
        Bytecode::Ret,
    ]);
    let errors = CodeUnitVerifier::verify(&module);
    assert_eq!(
        errors[0].major_status,
        StatusCode::NEGATIVE_STACK_SIZE_WITHIN_BLOCK
    );
}

#[test]
fn two_pop_no_push() {
    let module = file_format::dummy_procedure_module(vec![Bytecode::WriteRef, Bytecode::Ret]);
    let errors = CodeUnitVerifier::verify(&module);
    assert_eq!(
        errors[0].major_status,
        StatusCode::NEGATIVE_STACK_SIZE_WITHIN_BLOCK
    );
}


