language/bytecode_verifier/bytecode_verifier_tests/src/unit_tests/unused_entry_tests.rs
=======================================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use proptest::prelude::*;
use solana_libra_bytecode_verifier::UnusedEntryChecker;
use solana_libra_types::{identifier::Identifier, vm_error::StatusCode};
use solana_libra_vm::file_format::{
    CompiledModule, FieldDefinition, IdentifierIndex, LocalsSignature, ModuleHandleIndex,
    SignatureToken, StructHandle, StructHandleIndex, TypeSignature, TypeSignatureIndex,
};

proptest! {
    #[test]
    fn unused_locals_signature(module in CompiledModule::valid_strategy(10)) {
        let mut module = module.into_inner();
        module.locals_signatures.push(LocalsSignature(vec![]));
        let module = module.freeze().unwrap();
        let unused_entry_checker = UnusedEntryChecker::new(&module);
        prop_assert!(!unused_entry_checker.verify().is_empty());
    }
}

proptest! {
    #[test]
    fn unused_type_signature(module in CompiledModule::valid_strategy(10)) {
        let mut module = module.into_inner();
        module.type_signatures.push(TypeSignature(SignatureToken::Bool));
        let module = module.freeze().unwrap();
        let unused_entry_checker = UnusedEntryChecker::new(&module);
        prop_assert!(!unused_entry_checker.verify().is_empty());
    }
}

proptest! {
    #[test]
    fn unused_field(module in CompiledModule::valid_strategy(10)) {
        let mut module = module.into_inner();

        let type_sig_idx = module.type_signatures.len() as u16;
        module.type_signatures.push(TypeSignature(SignatureToken::Bool));

        let struct_name_idx = module.identifiers.len() as u16;
        module.identifiers.push(Identifier::new("foo".to_string()).unwrap());

        let field_name_idx = module.identifiers.len() as u16;
        module.identifiers.push(Identifier::new("bar".to_string()).unwrap());

        let sh_idx = module.struct_handles.len() as u16;
        module.struct_handles.push(StructHandle{
            module: ModuleHandleIndex::new(0),
            name: IdentifierIndex::new(struct_name_idx),
            is_nominal_resource: false,
            type_formals: vec![],
        });

        module.field_defs.push(FieldDefinition{
            struct_: StructHandleIndex::new(sh_idx),
            name: IdentifierIndex::new(field_name_idx),
            signature: TypeSignatureIndex::new(type_sig_idx),
        });

        let module = module.freeze().unwrap();
        let unused_entry_checker = UnusedEntryChecker::new(&module);

        let errs = unused_entry_checker.verify();

        let has_unused_fields = errs.iter().any(|err| {
            match err.major_status {
                StatusCode::UNUSED_FIELD => true,
                _ => false,
            }
        });

        let has_unused_type_signature = errs.iter().any(|err| {
            match err.major_status {
                StatusCode::UNUSED_TYPE_SIGNATURE => true,
                _ => false,
            }
        });

        prop_assert!(has_unused_fields && has_unused_type_signature);
    }
}


