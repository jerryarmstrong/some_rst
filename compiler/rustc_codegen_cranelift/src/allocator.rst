compiler/rustc_codegen_cranelift/src/allocator.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Allocator shim
// Adapted from rustc

use crate::prelude::*;

use rustc_ast::expand::allocator::{AllocatorKind, AllocatorTy, ALLOCATOR_METHODS};
use rustc_session::config::OomStrategy;
use rustc_span::symbol::sym;

/// Returns whether an allocator shim was created
pub(crate) fn codegen(
    tcx: TyCtxt<'_>,
    module: &mut impl Module,
    unwind_context: &mut UnwindContext,
) -> bool {
    let any_dynamic_crate = tcx.dependency_formats(()).iter().any(|(_, list)| {
        use rustc_middle::middle::dependency_format::Linkage;
        list.iter().any(|&linkage| linkage == Linkage::Dynamic)
    });
    if any_dynamic_crate {
        false
    } else if let Some(kind) = tcx.allocator_kind(()) {
        codegen_inner(
            module,
            unwind_context,
            kind,
            tcx.alloc_error_handler_kind(()).unwrap(),
            tcx.sess.opts.unstable_opts.oom,
        );
        true
    } else {
        false
    }
}

fn codegen_inner(
    module: &mut impl Module,
    unwind_context: &mut UnwindContext,
    kind: AllocatorKind,
    alloc_error_handler_kind: AllocatorKind,
    oom_strategy: OomStrategy,
) {
    let usize_ty = module.target_config().pointer_type();

    for method in ALLOCATOR_METHODS {
        let mut arg_tys = Vec::with_capacity(method.inputs.len());
        for ty in method.inputs.iter() {
            match *ty {
                AllocatorTy::Layout => {
                    arg_tys.push(usize_ty); // size
                    arg_tys.push(usize_ty); // align
                }
                AllocatorTy::Ptr => arg_tys.push(usize_ty),
                AllocatorTy::Usize => arg_tys.push(usize_ty),

                AllocatorTy::ResultPtr | AllocatorTy::Unit => panic!("invalid allocator arg"),
            }
        }
        let output = match method.output {
            AllocatorTy::ResultPtr => Some(usize_ty),
            AllocatorTy::Unit => None,

            AllocatorTy::Layout | AllocatorTy::Usize | AllocatorTy::Ptr => {
                panic!("invalid allocator output")
            }
        };

        let sig = Signature {
            call_conv: module.target_config().default_call_conv,
            params: arg_tys.iter().cloned().map(AbiParam::new).collect(),
            returns: output.into_iter().map(AbiParam::new).collect(),
        };

        let caller_name = format!("__rust_{}", method.name);
        let callee_name = kind.fn_name(method.name);

        let func_id = module.declare_function(&caller_name, Linkage::Export, &sig).unwrap();

        let callee_func_id = module.declare_function(&callee_name, Linkage::Import, &sig).unwrap();

        let mut ctx = Context::new();
        ctx.func.signature = sig.clone();
        {
            let mut func_ctx = FunctionBuilderContext::new();
            let mut bcx = FunctionBuilder::new(&mut ctx.func, &mut func_ctx);

            let block = bcx.create_block();
            bcx.switch_to_block(block);
            let args = arg_tys
                .into_iter()
                .map(|ty| bcx.append_block_param(block, ty))
                .collect::<Vec<Value>>();

            let callee_func_ref = module.declare_func_in_func(callee_func_id, &mut bcx.func);
            let call_inst = bcx.ins().call(callee_func_ref, &args);
            let results = bcx.inst_results(call_inst).to_vec(); // Clone to prevent borrow error

            bcx.ins().return_(&results);
            bcx.seal_all_blocks();
            bcx.finalize();
        }
        module.define_function(func_id, &mut ctx).unwrap();
        unwind_context.add_function(func_id, &ctx, module.isa());
    }

    let sig = Signature {
        call_conv: module.target_config().default_call_conv,
        params: vec![AbiParam::new(usize_ty), AbiParam::new(usize_ty)],
        returns: vec![],
    };

    let callee_name = alloc_error_handler_kind.fn_name(sym::oom);

    let func_id =
        module.declare_function("__rust_alloc_error_handler", Linkage::Export, &sig).unwrap();

    let callee_func_id = module.declare_function(&callee_name, Linkage::Import, &sig).unwrap();

    let mut ctx = Context::new();
    ctx.func.signature = sig;
    {
        let mut func_ctx = FunctionBuilderContext::new();
        let mut bcx = FunctionBuilder::new(&mut ctx.func, &mut func_ctx);

        let block = bcx.create_block();
        bcx.switch_to_block(block);
        let args = (&[usize_ty, usize_ty])
            .iter()
            .map(|&ty| bcx.append_block_param(block, ty))
            .collect::<Vec<Value>>();

        let callee_func_ref = module.declare_func_in_func(callee_func_id, &mut bcx.func);
        bcx.ins().call(callee_func_ref, &args);

        bcx.ins().trap(TrapCode::UnreachableCodeReached);
        bcx.seal_all_blocks();
        bcx.finalize();
    }
    module.define_function(func_id, &mut ctx).unwrap();
    unwind_context.add_function(func_id, &ctx, module.isa());

    let data_id = module.declare_data(OomStrategy::SYMBOL, Linkage::Export, false, false).unwrap();
    let mut data_ctx = DataContext::new();
    data_ctx.set_align(1);
    let val = oom_strategy.should_panic();
    data_ctx.define(Box::new([val]));
    module.define_data(data_id, &data_ctx).unwrap();
}


